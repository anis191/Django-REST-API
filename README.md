# PhiMart - REST API for an eCommerce Platform

![Django](https://img.shields.io/badge/Django-5.1.7-green)
![DRF](https://img.shields.io/badge/djangorestframework-3.15.2-red)
![JWT](https://img.shields.io/badge/JWT_Authentication-5.5.0-yellow)

A robust RESTful API for an eCommerce platform built with Django REST Framework. PhiMart provides comprehensive endpoints to manage users, products, shopping carts, orders, and more, following modern API design practices.

## 🚀 Key Features
- **JWT Authentication** (Token-Based Security)
- **User Management**: Registration, Login, and Profile Management
- **Product Catalog**: Full CRUD Operations for Products
- **Advanced Search & Filters**: Find products by category, price range, ratings, etc.
- **Shopping Cart System**: Add/Remove items, manage quantities
- **Order Management**: Create orders, view order history, and update status
- **Pagination**: Optimized for large datasets
- **API Documentation**: Interactive Swagger & ReDoc support
- **Social Auth Integration**: Via `social-auth-app-django`

## 🛠️ Technologies & Frameworks
- **Backend**: Django 5.1.7, Django REST Framework 3.15.2
- **Authentication**: JWT (SimpleJWT), Djoser
- **Database**: SQLite (Default Django DB)
- **Image Handling**: Pillow
- **API Docs**: drf-yasg (Swagger/ReDoc)
- **Filtering**: django-filter
- **Dependencies**: See [requirements.txt](requirements.txt)

## 📚 API Documentation
Explore endpoints interactively *(Localhost only)*:
- **Swagger UI**: http://127.0.0.1:8000/swagger/
- **ReDoc**: http://127.0.0.1:8000/redoc/

## 🔧 Installation & Local Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/anis191/Django-REST-API.git
   cd PhiMart
   ```
2. **Create & activate virtual environment**
   ```bash
   python -m venv .phi_env
    source .phi_env/Scripts/activate  # For Windows
    ```
3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```
4. **Run migrations**
   ```bash
   python manage.py migrate
   ```
5. **Start development server**
   ```bash
   python manage.py runserver
   ```
* API Access:
[http://127.0.0.1:8000/](http://127.0.0.1:8000/) *(Localhost only)*

## 🔒 Authentication
This API uses **JWT Tokens** for secure access.

### 📌 Endpoints  
**Base URL:** `http://127.0.0.1:8000/api/v1`

- `POST /auth/jwt/create/` – Obtain tokens (Login)  
- `POST /auth/jwt/refresh/` – Refresh tokens  
- `POST /auth/users/` – User registration

## 📂 Project Structure

`Django-REST-API/`  
&emsp;├── `PhiMart/` – Main Django project folder (Django settings and URLs)  
&emsp;│&emsp;├── `__init__.py`  
&emsp;│&emsp;├── `asgi.py`  
&emsp;│&emsp;├── `settings.py`  
&emsp;│&emsp;├── `urls.py`  
&emsp;│&emsp;└── `wsgi.py`  
&emsp;│  
&emsp;├── `api/` – Implements all API endpoints (urls)  
&emsp;│&emsp;├── `__init__.py`  
&emsp;│&emsp;├── `views.py`  
&emsp;│&emsp;├── `serializers.py`  
&emsp;│&emsp;├── `urls.py`  
&emsp;│&emsp;└── *(other supporting files)*  
&emsp;│  
&emsp;├── `fixtures/` – Contains demo data for database  
&emsp;│&emsp;└── `product_data.json` – Used to load sample product data  
&emsp;│  
&emsp;├── `media/`  
&emsp;│&emsp;└── `products/`  
&emsp;│&emsp;&emsp;└── `images/` – Stores uploaded product images  
&emsp;│  
&emsp;├── `order/` – Manages both order and cart-related features  
&emsp;│&emsp;├── `models.py`  
&emsp;│&emsp;├── `views.py`  
&emsp;│&emsp;├── `serializers.py`  
&emsp;│&emsp;├── `urls.py`  
&emsp;│&emsp;└── *(other supporting files)*  
&emsp;│  
&emsp;├── `product/` – Handles product-related logic  
&emsp;│&emsp;└── *(models, views, serializers, urls, etc.)*  
&emsp;│  
&emsp;├── `users/` – User authentication, profiles, registration  
&emsp;│&emsp;└── *(models, views, serializers, urls, etc.)*  
&emsp;│  
&emsp;├── `.gitignore` – Git ignore rules  
&emsp;├── `manage.py` – Django management script  
&emsp;└── `requirements.txt` – Project dependencies  

## 🤝 Contributing

Contributions help make this project better and are always welcome!

### How to Contribute

- ⭐ Star the repo  
- 🍴 Fork the project  
- 📥 Clone your fork  
- 💡 Create a feature branch: `git checkout -b feature/awesome-feature`  
- ✅ Commit your changes: `git commit -m 'Add some feature'`  
- 📤 Push your branch: `git push origin feature/awesome-feature`  
- 🛠️ Open a Pull Request

Ensure your code follows the project standards and passes all tests.

## 💻 Author

[**Anisul Alam**](https://github.com/anis191)  
Backend Developer | Django & REST APIs  
[🔗 LinkedIn](https://www.linkedin.com/in/anisul-alam-a330042a9/)

---
