from db.database import engine
from models import user, task #import all models so SQLAlchemy knows them

#create all tables defined in the imported models
user.Base.metadata.create_all(bind=engine)
task.Base.metadata.create_all(bind=engine)


print("Tables created successfully")