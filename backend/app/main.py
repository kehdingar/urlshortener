from fastapi import FastAPI, Response
from fastapi.middleware.cors import CORSMiddleware

from app.models import url

from app.database.config import engine

from app.api import shortener

from prometheus_client import generate_latest, CONTENT_TYPE_LATEST

# Code to enable prometheus.py middleware
from middleware.prometheus import track_requests



app = FastAPI(root_path="/api/v1")

url.Base.metadata.create_all(bind=engine)

# Enabling middleware
app.middleware("http")(track_requests)

# Endpoint returns metrics from prometheus
@app.get("/metrics",include_in_schema=False)
async def metrics():
    return Response(generate_latest(), media_type=CONTENT_TYPE_LATEST)

# Define the CORS middleware
origins = [
    "http://localhost:80",
    "http://localhost:8000",
    "http://localhost:8080",
    "http://localhost:3000",
    "http://localhost:9090",    
    "http://127.0.0.1:3000",
    "http://127.0.0.1:8000",
    "http://127.0.0.1",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {"message": "Welcome to the FastAPI application - URL Shortener!"}

app.include_router(shortener.router, prefix="/shortener", tags=["shortener"])
