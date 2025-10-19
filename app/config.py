import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    USER_EMAIL = os.getenv("USER_EMAIL", "example@example.com")
    USER_NAME = os.getenv("USER_NAME", "Anonymous")
    USER_STACK = os.getenv("USER_STACK", "Python/FastAPI")
