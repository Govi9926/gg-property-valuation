import fastapi
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from passlib.context import CryptContext
from models.user import * 
from db.database import get_db




pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def get_password_hash(password: str) -> str:
    return pwd_context.hash(password)


async def create_user_service(db: Session):
    # check if email already exists
    db_user = db.query(User).filter(User.email == User.email).first()
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")

    hashed_pw = get_password_hash(User.gaurav)

    new_user = User(
        username=User.username,
        email=User.email,
        full_name=User.full_name,
        hashed_password=hashed_pw,
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user
