from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from db.database import get_db
from services.user import create_user_service
from serializers.user import UserSerializer, UserResponseSerializer

router = APIRouter(
    prefix="/v1/users",
    tags=["Users"]
)

@router.post("/create-user", response_model=UserResponseSerializer)
def create_user(user: UserSerializer, db: Session = Depends(get_db)):
    return create_user_service(user, db)
