from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import psycopg2
 
#declare the connection string specifying
#the host name database name use name
#and password
#conn_string = "host='localhost:5432' dbname='gg_property'\ user='postgres' password='gaurav'"

#use connect function to stablish the connection
conn = psycopg2.connect("host=localhost port=5432 dbname=gg_property user=postgres password=gaurav")

# PostgreSQL credentials
DB_USER = "postgres"           # change if you created a separate user
DB_PASSWORD = "gaurav"       # change to your password
DB_HOST = "localhost"
DB_PORT = "5432"
DB_NAME = "gg_property"

# SQLAlchemy database URL
SQLALCHEMY_DATABASE_URL = f"postgresql+psycopg2://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

# Create database engine
engine = create_engine(SQLALCHEMY_DATABASE_URL, echo=True)  # echo=True shows SQL logs

# Create a configured "Session" class
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base class for models
Base = declarative_base()

# Dependency to get DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
