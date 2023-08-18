from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(root_path="/api/v1")


origins = [
    "http://localhost:80",
    "http://localhost:8000",
    "http://localhost:8080",
    "http://localhost:3000",
    "https://example.com",
    "https://www.example.com",
    "http://127.0.0.1:3001",
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
    return {"message": "Welcome to the FastAPI URL Shortener application!"}

