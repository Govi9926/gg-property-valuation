from fastapi import FastAPI , Depends, HTTPException
from routers import user, task   # import as modules
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session
from db.database import get_db

#create the FastAPI app
app = FastAPI()

# Include routers
app.include_router(task.router)
app.include_router(user.router)

#Define sqlalchemy models
Base = declarative_base()

class Item(Base) :
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    email = Column(String, index = True)

    

#setup the database connection 

DATABASE_URL = "postgresql://postgres:gaurav@localhost/gg_property"
engine = create_engine(DATABASE_URL)
'''
#create tables 
from . import models

print("Creating tables...")

#Create the database tables
Base.metadata.create_all(bind=engine)

print("Tables created!")'''

#create a sessionmaker object to interact with the database
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.clos()

#example endpoint to retrive an item by id
@app.get("/users/{item_id}")
def read_item(item_id: int, db: Session = Depends(get_db)):
    item = db.query(Item).filter(Item.id == item.id).first()
    if item is None:
        raise HTTPException(status_code=404, detail="Item not Found")
    return item
