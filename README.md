# VisionMate Dashboard

## Installation

### Requirements
Để chạy ứng dụng này, bạn cần cài đặt các thư viện sau:

```bash
pip install -r requirements.txt
```

Hoặc sử dụng virtual environment (khuyến nghị):

```bash
# Tạo virtual environment
python -m venv venv

# Kích hoạt virtual environment
venv\Scripts\activate

# Cài đặt requirements
pip install -r requirements.txt
```

## Cấu trúc Template

Project sử dụng Flask với Jinja2 template engine và tuân theo cấu trúc:

- `templates/base.html`: Template gốc chứa layout chính
- `partials/sidebar.html`: Sidebar navigation
- `partials/navbar.html`: Top navigation bar
- `pages/`: Các trang cụ thể kế thừa từ base template

## Chạy ứng dụng
```bash
python app.py
```