# app/db/dependencies.py
from typing import Generator
from sqlalchemy.orm import Session
from app.db.database import SessionLocal  # ✅ import correto, sem circularidade

def get_db() -> Generator[Session, None, None]:
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()