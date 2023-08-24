

def test_create_url(test_client, test_db):
    # Create a URL using the test client
    response = test_client.post(
        "/api/v1/shortener/urls",
        json={"full_url": "https://www.example.com"},
    )

    # Assert that the response has a successful status code
    assert response.status_code == 200

    # Assert that the response body contains the expected data
    data = response.json()
    assert "full_url" in data
    assert "short_url" in data
    assert data["full_url"] == "https://www.example.com"

def test_missing_scheme(test_client):
    response = test_client.post("/api/v1/shortener/urls", json={"full_url": "missing_scheme_url"})
    assert response.status_code == 422
    assert response.json() == {'detail': 'URL must have a valid scheme (http/https)'}

def test_no_domain(test_client):
    response = test_client.post("/api/v1/shortener/urls", json={"full_url": "https://www"})
    assert response.status_code == 422
    assert response.json() == {'detail': 'Invalid URL format: missing dot in domain'}