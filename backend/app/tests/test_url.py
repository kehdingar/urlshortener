import time
from app.models.url import URL
import urllib.parse



def test_create_url(test_client, test_db):
    # Create a URL using the test client
    response = test_client.post(
        "/api/v1/shortener",
        json={"full_url": "http://example.com"},
    )

    # Assert that the response has a successful status code
    assert response.status_code == 200

    # Assert that the response body contains the expected data
    data = response.json()
    assert "task_id" in data

def test_missing_scheme(test_client):
    response = test_client.post("/api/v1/shortener", json={"full_url": "missing_scheme_url"})
    assert response.status_code == 422
    assert response.json()['detail']['error'] == 'URL must have a valid scheme (http/https)'

def test_no_domain(test_client):
    response = test_client.post("/api/v1/shortener", json={"full_url": "https://www"})
    assert response.status_code == 422
    assert response.json()['detail']['error']  == 'Invalid URL format: missing dot in domain'


def test_get_task_result(test_client):
    # Test getting task result for a completed task
    url_create_data = {"full_url": "http://example.com"}
    response = test_client.post("/api/v1/shortener", json=url_create_data)
    task_id = response.json()["task_id"]

    # Wait for the task to complete
    response = test_client.get(f"/api/v1/shortener/task/{task_id}")
    data = response.json()

    verify = data["status"]

    while verify != "completed":
        response = test_client.get(f"/api/v1/shortener/task/{task_id}")
        # Simulating delay of task
        time.sleep(3)
        verify = response.json()["status"]

    assert response.status_code == 200
    assert response.json()['status'] == "completed"
    assert response.json()['status'] != ""
    assert response.json()['status'] != ""

def test_get_task_result_pending(test_client):
    # Test getting task result for a pending task
    url_create_data = {"full_url": "http://example2.com"}
    response = test_client.post("/api/v1/shortener", json=url_create_data)
    task_id = response.json()["task_id"]

    # Task is still pending
    response = test_client.get(f"/api/v1/shortener/task/{task_id}")
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "pending"
    assert data["full_url"] == ""
    assert data["short_url"] == ""

def test_duplicate(test_client):
    # Test getting task result for a pending task
    url_create_data = {"full_url": "http://example.com"}
    response = test_client.post("/api/v1/shortener", json=url_create_data)
    # Task is still pending
    assert 'URL already exists' in response.json()['detail']['error']
    assert 'short_url' in response.json()['detail']


def test_get_url(test_client, test_db):
    # Create a URL in the database to retrieve
    session = test_db()
    url = session.query(URL).filter(URL.full_url == 'http://example.com').first()

    # Send a GET request to retrieve the URL by its short URL
    response = test_client.get(f"/api/v1/shortener/short_url/{url.short_url}")

    data = response.json()
    assert response.status_code == 200
    assert "full_url" in data
    assert data["full_url"] == "http://example.com"
