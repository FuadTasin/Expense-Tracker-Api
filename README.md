# Expense Tracker API

A RESTful Expense Tracker API built with **FastAPI**, **SQLAlchemy**, and **PostgreSQL**. It provides user authentication and transaction management, allowing users to securely manage their income and expenses.

## 🚀 Live Demo

- **Live API:** https://expense-tracker-api-cgo5.onrender.com
- **API Documentation (Swagger UI):** https://expense-tracker-api-cgo5.onrender.com/docs

## 🛠️ Technologies Used

- **Python** – Backend programming language
- **FastAPI** – REST API development
- **SQLAlchemy** – ORM for database operations
- **PostgreSQL** – Database
- **Pydantic** – Data validation
- **JWT (JSON Web Tokens)** – Authentication
- **Passlib & Bcrypt** – Password hashing
- **Render** – API deployment
- **Supabase** – PostgreSQL database hosting

## ✨ Features

### Authentication
- User registration
- Secure password hashing
- User login
- JWT-based authentication
- Protected API endpoints

### Transaction Management
- Create income and expense transactions
- Retrieve all transactions
- Retrieve a specific transaction
- Update transaction details
- Delete transactions
- Filter transactions by type, category, and amount range

### Security
- Passwords are stored as hashed values.
- JWT tokens are used for authentication.
- Users can access only their own transactions.

## 📁 Project Structure

```text
Expense-Tracker-Api/
│
├── router/
│   ├── authentication.py
│   └── tokens.py
│
├── database.py
├── dependencies.py
├── main.py
├── models.py
├── schemas.py
├── transactions.py
├── requirements.txt
├── .gitignore
└── README.md
```

## ⚙️ Installation and Setup

### 1. Clone the repository

```bash
git clone https://github.com/FuadTasin/Expense-Tracker-Api.git
```

### 2. Navigate to the project directory

```bash
cd Expense-Tracker-Api
```

### 3. Create a virtual environment

```bash
python -m venv .venv
```

Activate it:

**macOS / Linux**
```bash
source .venv/bin/activate
```

**Windows**
```bash
.venv\Scripts\activate
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

### 5. Configure environment variables

Create a `.env` file in the project root directory.

```env
SQLALCHEMY_DATABASE_URL=your_postgresql_database_url
SECRET_KEY=your_secret_key
ALGORITHM=HS256
```

Replace the placeholders with your own credentials.

### 6. Run the application

```bash
uvicorn main:app --reload
```

The application will run at:

```text
http://127.0.0.1:8000
```

Access the interactive API documentation:

```text
http://127.0.0.1:8000/docs
```

## 📌 API Endpoints

### Authentication

| Method | Endpoint | Description |
|---|---|---|
| POST | `/auth/registration` | Register a new user |
| POST | `/auth/login` | Login and obtain JWT token |

### Transactions

| Method | Endpoint | Description |
|---|---|---|
| GET | `/transactions` | Get all user transactions |
| GET | `/transactions/{transaction_id}` | Get a specific transaction |
| POST | `/transactions/create` | Create a transaction |
| POST | `/transactions/update/{transaction_id}` | Update a transaction |
| DELETE | `/transactions/delete/{transaction_id}` | Delete a transaction |
| GET | `/transactions/filter` | Filter transactions |

## 🔐 Authentication

The API uses JWT-based authentication.

1. Register an account.
2. Log in using your username and password.
3. Receive an access token.
4. Use the token to access protected endpoints.

In Swagger UI, click **Authorize** and provide your login credentials through the OAuth2 form.

## 🚀 Deployment

The API is deployed using **Render**, while PostgreSQL is hosted on **Supabase**.

Environment variables are configured directly in the Render dashboard rather than committed to the repository.

## 👨‍💻 Author

**Fuad Tasin**

- GitHub: [@FuadTasin](https://github.com/FuadTasin)
