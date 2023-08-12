import pytest


@pytest.fixture(autouse=True)
def envs_db(monkeypatch):
    monkeypatch.setenv("uri", "")
