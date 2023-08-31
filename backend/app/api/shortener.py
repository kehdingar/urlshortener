from fastapi import APIRouter,Depends
from app.schemas.url import URLCreate, URLReturn, TaskStatus, GetUrlRequest
from starlette.exceptions import HTTPException
from sqlalchemy.orm import Session
from app.database.config import get_db
from app.models.url import URL
from celery.result import AsyncResult
from celery import Celery
from app.api.celery_utils import celery
from celery.result import AsyncResult
import urllib.parse


router = APIRouter()


# API endpoint for creating a URL
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

# API endpoint for getting tasks result
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

# API endpoint for retrieving a URL by its short URL
@router.get("/short_url/{short_url:path}")
def get_url(short_url: str,db: Session = Depends(get_db)):

    short_url = urllib.parse.unquote(short_url)

    db_url = db.query(URL).filter(URL.short_url == short_url).first()  

    print(db_url)
    # If the URL is not found, raise an HTTPException
    if db_url is None:
        raise HTTPException(status_code=404, detail="URL not found")

    return GetUrlRequest(full_url=db_url.full_url)