


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