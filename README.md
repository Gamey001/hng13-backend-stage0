# 🧙‍♂️ Backend Wizards — Stage 0 Task (FastAPI Implementation)

## 🚀 Overview

A simple FastAPI endpoint that returns your profile info and a random cat fact fetched from [Cat Facts API](https://catfact.ninja/fact).

---

## 📍 Endpoint

**GET /me**

### Example Response

```json
{
  "status": "success",
  "user": {
    "email": "youremail@example.com",
    "name": "Your Full Name",
    "stack": "Python/FastAPI"
  },
  "timestamp": "2025-10-19T11:52:23.789Z",
  "fact": "Cats sleep for around 13 to 14 hours a day."
}
```
