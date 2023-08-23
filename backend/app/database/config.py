from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker
import os
from dotenv import load_dotenv,find_dotenv

load_dotenv()
dotenv_path = find_dotenv(raise_error_if_not_found=True, usecwd=True)
load_dotenv(dotenv_path)

if os.getenv("TESTING"):
    SQLALCHEMY_DATABASE_URL = "sqlite:///test.db"
    # When about to start test for the first time,set the python environment varaible on commandline to be true like so
    # command : export TESTING=1
    # then run test in this case - command : pytest app/tests -v
else:
    SQLALCHEMY_DATABASE_URL = os.environ.get("APP_DATABASE_URL")

engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
