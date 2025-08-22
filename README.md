# PhiMart - REST API for an eCommerce Platform

![Django](https://img.shields.io/badge/Django-5.1.7-green)
![DRF](https://img.shields.io/badge/djangorestframework-3.15.2-red)
![JWT](https://img.shields.io/badge/JWT_Authentication-5.5.0-yellow)
![Payments](https://img.shields.io/badge/Payments-SSLCommerz-blue)

A robust RESTful API for an eCommerce platform built with Django REST Framework. PhiMart provides comprehensive endpoints to manage users, products, shopping carts, orders, and more, following modern API design practices.

## 🌐 Live Deployment

- 🔗 **Base URL** – [https://phimart-ecommerce-wheat.vercel.app/](https://phimart-ecommerce-wheat.vercel.app/)
- 🔗 **API Root** – [https://phimart-ecommerce-wheat.vercel.app/api/v1/](https://phimart-ecommerce-wheat.vercel.app/api/v1/)


## 🚀 Key Features
- **JWT Authentication** (Token-Based Security)
- **User Management**: Registration, Login, and Profile Management
- **Product Catalog**: Full CRUD Operations for Products
- **Advanced Search & Filters**: Find products by category, price range, ratings, etc.
- **Shopping Cart System**: Add/Remove items, manage quantities
- **Order Management**: Create orders, view order history, and update status
- **Secure Payment Integration**: Integrated with **SSLCommerz** for payment processing
- **Pagination**: Optimized for large datasets
- **API Documentation**: Interactive Swagger & ReDoc support
- **Social Auth Integration**: Via `social-auth-app-django`

## 💳 Payment Feature
PhiMart now supports **online payments** using **SSLCommerz**.  

### 🔑 Endpoints
| Method | Endpoint | Description |
|--------|----------|-------------|
| `POST` | `/api/v1/payment/initiate/` | Start a new payment session with SSLCommerz |
| `POST` | `/api/v1/payment/success/` | Callback for successful payment – updates order status to **Paid** |
| `POST` | `/api/v1/payment/cancel/` | Callback for canceled payment – marks order as **Canceled** |
| `POST` | `/api/v1/payment/fail/` | Callback for failed payment – marks order as **Failed** |

✅ Additional utility:
- `GET /api/v1/orders/has_ordered/<int:product_id>/` → Check if a user has purchased a specific product (useful for **review eligibility**).  

Payment workflow ensures that only valid orders can be paid for, with secure redirection to SSLCommerz and proper callback handling.

## 🛠️ Technologies & Frameworks
- **Backend**: Django 5.1.7, Django REST Framework 3.15.2
- **Authentication**: JWT (SimpleJWT), Djoser
- **Database**: SQLite (Default Django DB)
- **Image Handling**: Pillow
- **API Docs**: drf-yasg (Swagger/ReDoc)
- **Filtering**: django-filter
- **Dependencies**: See [requirements.txt](requirements.txt)

## 📚 API Documentation
Explore the live interactive API documentation:
- **Swagger UI**: https://phimart-ecommerce-wheat.vercel.app/swagger/
- **ReDoc**: https://phimart-ecommerce-wheat.vercel.app/redoc/

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
4. **Set up environment variables**  
   Create a `.env` file in the project root and configure it as follows:

   ```bash
   # Django Secret
   SECRET_KEY=your_secret_key
   DEBUG=True

   # Database (PostgreSQL)
   DB_USER=your_db_user
   DB_PASSWORD=your_db_password
   DB_HOST=your_db_host
   DB_PORT=your_db_port
   DB_NAME=your_db_name

   # Cloudinary (for media uploads)
   CLOUD_NAME=your_cloud_name
   CLOUDINARY_API_KEY=your_api_key
   CLOUDINARY_API_SECRET=your_api_secret
   CLOUDINARY_URL=cloudinary://your_api_key:your_api_secret@your_cloud_name

   # Email Configuration
   EMAIL_HOST=your_email_host
   EMAIL_PORT=your_email_port
   EMAIL_USE_TLS=True
   EMAIL_HOST_USER=your_email_address
   EMAIL_HOST_PASSWORD=your_email_app_password

   # Frontend Integration
   FRONTEND_PROTOCOL=http
   FRONTEND_DOMAIN=localhost:5173
   FRONTEND_URL=http://localhost:5173

   # Backend URL
   BACKEND_URL=http://127.0.0.1:8000

   # Payment (SSLCommerz)
   SSLCommerz_STORE_ID=your_store_id
   SSLCommerz_STORE_PASSWORD=your_store_password
   ```
5. **Run migrations**
   ```bash
   python manage.py migrate
   ```
6. **Start development server**
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
