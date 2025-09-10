from fastapi import FastAPI
from routers import task

app = FastAPI()

# Include the router from the tasks module
app.include_router(task.router)

@app.get("/")
def read_root():
    return {"message": "FastAPI is running!"}
