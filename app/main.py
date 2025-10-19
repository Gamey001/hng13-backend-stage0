from fastapi import FastAPI
from fastapi.responses import JSONResponse
from datetime import datetime, timezone
from app.config import Config
from app.utils.cats_facts import fetch_cat_fact

app = FastAPI(
    title="Backend Wizards Stage 0",
    description="A simple FastAPI endpoint returning profile info and a random cat fact.",
    version="1.0.0"
)

@app.get("/me", response_class=JSONResponse)
async def get_profile():
    timestamp = datetime.now(timezone.utc).isoformat()

    response = {
        "status": "success",
        "user": {
            "email": Config.USER_EMAIL,
            "name": Config.USER_NAME,
            "stack": Config.USER_STACK
        },
        "timestamp": timestamp,
        "fact": fetch_cat_fact()
    }

    return JSONResponse(content=response, status_code=200)
