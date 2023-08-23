import os
import pytest
from fastapi.testclient import TestClient
from sqlalchemy.orm import sessionmaker
from app.main import app
from app.database.config import Base,engine
from dotenv import load_dotenv,find_dotenv


load_dotenv()
dotenv_path = find_dotenv(raise_error_if_not_found=True, usecwd=True)
load_dotenv(dotenv_path)

@pytest.fixture(scope="module")
def test_client():
    with TestClient(app) as client:
        yield client


@pytest.fixture(scope="session")
def test_db():
    # Create an in-memory SQLite database for testing
    TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    Base.metadata.create_all(bind=engine)

    # Provide a test session for the tests
    yield TestingSessionLocal

    # Clean up the test database after tests are finished
    Base.metadata.drop_all(bind=engine)
    # Remove database after tests are finished
    os.remove("./test.db")
