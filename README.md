# VisionMate - Flask Application with Advanced Architecture

## Cấu trúc dự án

Dự án này được xây dựng với cấu trúc hiện đại sử dụng:
- **Blueprint Architecture**: Chia nhỏ ứng dụng theo module
- **Class-based Views**: Tổ chức code tốt hơn, dễ tái sử dụng
- **JSON Route Configuration**: Quản lý routes linh hoạt
- **Route Decorators**: Bảo mật và validation

## Cấu trúc thư mục

```
Vision/
├── app.py                  # Entry point chính
├── requirements.txt        # Dependencies
├── config/
│   ├── app_config.py      # Cấu hình ứng dụng
│   └── routes.json        # Cấu hình routes
├── core/
│   └── route_loader.py    # Route loader engine
├── views/
│   ├── base.py           # Base view classes
│   ├── dashboard.py      # Dashboard views
│   ├── auth.py           # Authentication views
│   ├── management.py     # Management views
│   └── api.py            # API views
├── utils/
│   └── decorators.py     # Route decorators
├── templates/
│   ├── base.html
│   ├── errors/           # Error pages
│   └── pages/            # Application pages
└── static/               # CSS, JS, images
```

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

## Chạy ứng dụng
```bash
python app.py
```

## Truy cập ứng dụng
- Dashboard: http://localhost:5000/
- Sign In: http://localhost:5000/auth/sign-in
- Management: http://localhost:5000/management/users
- API: http://localhost:5000/api/v1/users

## Tài khoản demo
- Email: `admin@visionmate.com`
- Password: `admin123`

## Cấu trúc Template

Project sử dụng Flask với Jinja2 template engine và tuân theo cấu trúc:

- `templates/base.html`: Template gốc chứa layout chính
- `partials/sidebar.html`: Sidebar navigation
- `partials/navbar.html`: Top navigation bar
- `pages/`: Các trang cụ thể kế thừa từ base template