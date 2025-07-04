# app/crud.py

from sqlalchemy.orm import Session
from app import models, schemas

# Create a new task
def create_task(db: Session, task: schemas.TaskCreate, user_id: int):
    new_task = models.Task(
        title=task.title,
        description=task.description,
        due_date=task.due_date,
        is_completed=False,
        owner_id=user_id
    )
    db.add(new_task)
    db.commit()
    db.refresh(new_task)
    return new_task

# Get all tasks
def get_tasks(db: Session):
    return db.query(models.Task).all()

# Get tasks by user
def get_tasks_by_user(db: Session, user_id: int):
    return db.query(models.Task).filter(models.Task.owner_id == user_id).all()

# Get a single task by ID
def get_task(db: Session, task_id: int):
    return db.query(models.Task).filter(models.Task.id == task_id).first()

# Update a task
def update_task(db: Session, task_id: int, task_update: schemas.TaskUpdate):
    task = db.query(models.Task).filter(models.Task.id == task_id).first()
    if not task:
        return None

    for key, value in task_update.dict(exclude_unset=True).items():
        setattr(task, key, value)

    db.commit()
    db.refresh(task)
    return task

# Delete a task
def delete_task(db: Session, task_id: int):
    task = db.query(models.Task).filter(models.Task.id == task_id).first()
    if not task:
        return None
    db.delete(task)
    db.commit()
    return task 