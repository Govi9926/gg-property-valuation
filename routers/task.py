from fastapi import APIRouter

router = APIRouter(
    prefix="/tasks",
    tags=["Tasks"]
)

@router.get("/create-tast")
async def get_tasks():
    return {"message": "List of tasks"}

@router.post("/")
async def create_task():
    return {"message": "Task created"}
