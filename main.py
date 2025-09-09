from fastapi import FastAPI
from routers import user, task   # import as modules

app = FastAPI()

# Include routers
app.include_router(task.router)
app.include_router(user.router)
