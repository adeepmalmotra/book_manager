# Book Management System with Gen AI

This is a Python-based intelligent book management system using **FastAPI**, **PostgreSQL**, and **Llama 3** (or compatible GenAI models). It supports:

- CRUD operations on books and reviews
- Summary generation using a locally running Llama3 model
- Asynchronous API handling
- Docker/Cloud ready deployment

## ✅ Features
- Async FastAPI application with PostgreSQL (via `asyncpg` and SQLAlchemy)
- Integration with GenAI for summaries and recommendations
- Basic Authentication
- RESTful APIs
- Clean architecture adhering to SOLID principles
- Modular codebase with design patterns
- Swagger API docs
- Unit tests using Pytest

## 🚀 Setup Instructions

1. Clone the repo
2. Create a virtual environment and activate it
3. Install dependencies: `pip install -r requirements.txt`
4. Setup `.env` file as shown in `.env.example`
5. Run: `uvicorn app.main:app --reload`

## 📦 Deployment
You can use Docker, GitHub Actions, or AWS for deployment. Instructions coming soon.