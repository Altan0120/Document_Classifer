# Hệ Thống Phân Loại Văn Bản Tiếng Việt Sử Dụng PhoBERT 

Ứng dụng web hoàn chỉnh (End-to-End) cho phép người dùng nhập văn bản thô hoặc tải lên các định dạng tài liệu phổ biến (`.pdf`, `.docx`, `.txt`) để tự động phân loại vào 18 danh mục tin tức tiếng Việt khác nhau với độ chính xác cao.

---

## Cấu Trúc Thư Mục Hệ Thống

```text
Document_Classifier/
│
├── frontend/                  # Khối Giao diện người dùng (Frontend)
│   └── index.html             # Giao diện chính và logic trích xuất tài liệu
|
├── phobert_data/              # Khối Dữ liệu huấn luyện
│   └── label_mapping.json     # Từ điển ánh xạ ID số sang tên danh mục Tiếng Việt
│
├── phobert_news/              # BỘ NÃO AI (Không đẩy lên Git vì file nặng)
│   ├── config.json            # Cấu hình kiến trúc mạng của mô hình
│   ├── model.safetensors      # Trọng số mô hình đã huấn luyện (~515MB)
│   ├── tokenizer_config.json  # Cấu hình bộ mã hóa từ vựng
│   └── vocab.txt              # Từ điển từ vựng của PhoBERT
│
├── api.py                     # AI Server mở cổng API (FastAPI Backend)
├── requirements.txt           # Danh sách các thư viện Python cần cài đặt
└── .gitignore                 # Cấu hình chặn các file rác và file quá nặng lên Git
```
---

## Hướng dẫn cài đặt
### 1. Tải và thêm model cùng các file cấu hình vào thư mục ***/Document_Classifer/phobert_news***
[Link Drive](https://drive.google.com/drive/folders/1npZnpOrsWy05fsjYuPWNB1Yoxofto_A9?usp=sharing)

### 2. Cài đặt môi trường 
```bash
pip install -r requirement.txt
```

### 3. Khởi chạy ứng dụng 
```bash
python -m uvicorn api:app --port 8000 --reload
```
### 4. Giao diện Web
Mở trực tiếp file ***index.html***  


