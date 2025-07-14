# KPA Form Data API (Suvidhaen Assignment)

This project implements two backend APIs from the provided Swagger/Postman documentation using **FastAPI** and **PostgreSQL**.

## 🚀 Setup Instructions

1. Clone the repository  
   `git clone https://github.com/harichopper/kpa-api-assignment.git`

2. Install dependencies  
   `pip install -r requirements.txt`

3. Setup PostgreSQL and create a database named `kpa_db`.

4. Copy `.env.example` to `.env` and update with your DB credentials.

5. Run the app:  
   `uvicorn app.main:app --reload`

## 🧪 APIs Implemented

1. `POST /form/addData` – Add form data (name, email, phone, location)
2. `GET /form/getallData` – Get all submitted form data

## 🛠️ Tech Stack
- Python 3.11
- FastAPI
- SQLAlchemy (Async)
- PostgreSQL
- Pydantic

## 📂 Postman Collection
Postman collection available in:  
`kpa_form.postman_collection.json`

## 🎥 Submission Video
[Assignment Walkthrough](https://drive.google.com/your-video-link)

---

