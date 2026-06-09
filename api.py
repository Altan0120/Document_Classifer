import torch
import json
from pyvi import ViTokenizer
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from transformers import AutoModelForSequenceClassification, AutoTokenizer

app = FastAPI(title="PhoBERT News Classifier API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], 
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

print("Đang nạp bộ não PhoBERT vào bộ nhớ...")
MODEL_PATH = "./phobert_news"

tokenizer = AutoTokenizer.from_pretrained(MODEL_PATH)
model = AutoModelForSequenceClassification.from_pretrained(MODEL_PATH)
model.eval()

with open("phobert_data/label_mapping.json", "r", encoding="utf-8") as f:
    label_mapping = json.load(f)
    id2label = {v: k for k, v in label_mapping.items()}

print("✅ AI Server đã sẵn sàng nhận lệnh!")

class DocumentRequest(BaseModel):
    documentText: str

@app.post("/api/classify")
async def classify_text(request: DocumentRequest):
    raw_text = request.documentText
    
    segmented_text = ViTokenizer.tokenize(raw_text)
    words = segmented_text.split()

    if len(words) > 256:
        # Lấy 128 từ đầu và 128 từ cuối ghép lại
        head = words[:128]
        tail = words[-128:]
        segmented_text = " ".join(head + tail)

    inputs = tokenizer(
        segmented_text, 
        return_tensors="pt", 
        padding="max_length", 
        truncation=True, 
        max_length=256
    )
    
    with torch.no_grad():
        outputs = model(**inputs)
        logits = outputs.logits
        
    predicted_id = torch.argmax(logits, dim=-1).item()
    probabilities = torch.nn.functional.softmax(logits, dim=-1)
    confidence = probabilities[0][predicted_id].item() * 100
    
    category_name = id2label[predicted_id]
    
    return {
        "category": category_name,
        "confidence": round(confidence, 2)
    }