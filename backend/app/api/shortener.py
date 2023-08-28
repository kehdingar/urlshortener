from fastapi import APIRouter,Depends
from app.schemas.url import URLCreate, URLReturn, TaskStatus
from starlette.exceptions import HTTPException
from sqlalchemy.orm import Session
from app.database.config import get_db
from app.models.url import URL
from celery.result import AsyncResult
from celery import Celery
from app.api.celery_utils import celery
from celery.result import AsyncResult


router = APIRouter()


# Define the API endpoint for creating a URL
@router.post("/", response_model=dict)
async def create_url(url: URLCreate, db: Session = Depends(get_db)):
    # Check if the URL already exists in the database
    db_url = db.query(URL).filter(URL.full_url == url.full_url).first()
    if db_url:
        raise HTTPException(status_code=400, detail={'state':'Duplicate data','short_url': db_url.short_url})
    
    # Convert the URLCreate instance to a dictionary since pydantic models are
    # not directly serializable to JSON.
    url_dict = url.model_dump()

    task_result = celery.send_task("tasks.shorten_url", args=[url_dict])

    # Return the task ID to the client
    return {"task_id": task_result.id}

@router.get("/task/{task_id}", response_model=URLReturn)
async def get_task_result(task_id: str,db: Session = Depends(get_db)):
    # Use Celery to get the task result
    task_result = AsyncResult(task_id, app=celery)

    if task_result.ready():
        # If the task is completed, return the result
        result = task_result.result
        db_url = URL(full_url=result['full_url'], short_url=result['short_url'])
        db.add(db_url)
        db.commit()
        db.refresh(db_url)        
        return URLReturn(full_url= result['full_url'], short_url=result['short_url'], status=TaskStatus.completed)
    
    else:
        # If the task is still pending or running, return its status
        return URLReturn(full_url="", short_url="", status=TaskStatus.pending)