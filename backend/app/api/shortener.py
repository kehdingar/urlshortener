from fastapi import APIRouter,Depends
from app.schemas.url import URLCreate, URLReturn
from starlette.exceptions import HTTPException
from sqlalchemy.orm import Session
from app.database.config import get_db
from app.models.url import URL
import pyshorteners


router = APIRouter()


