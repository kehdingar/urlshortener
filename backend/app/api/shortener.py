from fastapi import APIRouter,Depends
from app.schemas.url import URLCreate, URLReturn
from starlette.exceptions import HTTPException
from sqlalchemy.orm import Session
from app.database.config import get_db
from app.models.url import URL
import pyshorteners


router = APIRouter()


# Define the API endpoint for creating a URL
@router.post("/urls", response_model=URLReturn)
def create_url(url: URLCreate, db: Session = Depends(get_db)):
    # Check if the URL already exists in the database
    db_url = db.query(URL).filter(URL.full_url == url.full_url).first()
    if db_url:
        raise HTTPException(status_code=400, detail="Duplicate data")
    
    # Generate a short URL using pyshorteners
    s = pyshorteners.Shortener()
    short_url = s.tinyurl.short(url.full_url)

    # Create a new URL in the database
    db_url = URL(full_url=url.full_url, short_url=short_url)
    db.add(db_url)
    db.commit()
    db.refresh(db_url)

    # Return the full and short URLs
    return URLReturn(full_url=db_url.full_url, short_url=db_url.short_url)