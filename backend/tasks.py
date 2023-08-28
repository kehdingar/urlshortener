from celery import Celery
from fastapi import APIRouter,Depends
from app.schemas.url import URLCreate, URLReturn
from starlette.exceptions import HTTPException
from sqlalchemy.orm import Session
from app.models.url import URL
import pyshorteners
from app.database.config import get_db
from app.api.celery_utils import celery

@celery.task
def shorten_url(url_dict):
    try:
        # Extract the URL from the dictionary
        full_url = url_dict.get("full_url")

        if not full_url:
            raise ValueError("URL not provided in the input dictionary")

        # Use pyshorteners to shorten the URL
        s = pyshorteners.Shortener()
        short_url = s.tinyurl.short(full_url)        
        return {'full_url': full_url, 'short_url':short_url}

    except Exception as e:
        # Handle any errors (e.g., invalid URLs)
        return f"Error: {e}"


