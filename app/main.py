from fastapi import FastAPI
from app.routers import task, user
from app.database import create_db

app = FastAPI(title="Task Manager API", description="FastAPI")

create_db()
app.include_router(task.router)
app.include_router(user.router)
@app.get("/")
def read_root():
    return {"message": "Welcome to the Task Manager API"}