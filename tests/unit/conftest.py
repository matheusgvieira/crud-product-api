import pytest
from fastapi.testclient import TestClient
from products_api.app import app


@pytest.fixture(autouse=True)
def envs_db(monkeypatch):
    monkeypatch.setenv("uri", "")


@pytest.fixture(scope="module")
def client():
    with TestClient(app) as client:
        yield client
