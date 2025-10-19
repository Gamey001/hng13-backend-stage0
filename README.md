# 🚀 HNG13 Backend Stage 0 — Profile Endpoint

This project is my submission for **Backend Wizards Stage 0** of the [HNG13 Internship](https://hng.tech/).  
The goal was to build a simple **FastAPI** endpoint that returns my profile information together with a **dynamic cat fact** fetched from an external API.

---

## 🔗 Live API URL
**Hosted on Railway:**  
👉 https://web-production-0489.up.railway.app/me  

**GitHub Repository:**  
👉 https://github.com/Gamey001/hng13-backend-stage0

---

## 🧠 Features
- Built with **FastAPI** 🐍  
- Returns JSON containing:
  - My profile details (name, email, stack)
  - Current UTC timestamp
  - A random cat fact from [catfact.ninja](https://catfact.ninja)
- Clean and modular project structure  
- Environment-based configuration using `.env`

---

## 📁 Project Structure

hng13-backend-stage0/
│
├── app/
│ ├── main.py
│ ├── config.py
│ ├── utils/
│ │ └── cat_fact.py
│ ├── init.py
│ └── utils/init.py
│
├── .env
├── requirements.txt
└── README.md


---

## ⚙️ Setup & Run Locally

### 1️⃣ Clone the repository
```bash
git clone https://github.com/Gamey001/hng13-backend-stage0.git
cd hng13-backend-stage0

2️⃣ Create a virtual environment
python3 -m venv venv
source venv/bin/activate

4️⃣ Create a .env file

In the project root, create a .env file and add your details:

USER_NAME= Your username
USER_EMAIL= xyz@example.com
USER_STACK= your stack

5️⃣ Run the app
uvicorn app.main:app --reload

Visit:
👉 http://127.0.0.1:8000/me

**You should see a response similar to:
{
  "status": "success",
  "user": {
    "name": "Gamaliel Dashua",
    "email": "gamalieldashua@example.com",
    "stack": "Backend (Python/FastAPI)"
  },
  "timestamp": "2025-10-19T14:32:45.123Z",
  "fact": "Cats sleep for around 13 to 14 hours a day."
}

🧩 Dependencies

**All dependencies are listed in requirements.txt

fastapi
uvicorn
requests
python-dotenv

**Install with:
pip install -r requirements.txt
