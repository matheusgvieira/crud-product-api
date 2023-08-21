import pytest


@pytest.mark.root
def test_root(client):
    response = client.get("/health")
    assert response.status_code == 200


@pytest.mark.root
def test_root(client):
    response = client.get("/health/database")
    assert response.status_code == 200
