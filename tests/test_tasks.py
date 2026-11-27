import pytest
from fastapi.testclient import TestClient

from app import main

client = TestClient(main.app)


@pytest.fixture(autouse=True)
def reset_state():
    main._tasks.clear()
    main._next_id = 1


def test_list_is_empty_at_start():
    assert client.get("/tasks").json() == []


def test_create_task():
    r = client.post("/tasks", json={"title": "write pipeline"})
    assert r.status_code == 201
    assert r.json() == {"id": 1, "title": "write pipeline"}


def test_create_then_list():
    client.post("/tasks", json={"title": "a"})
    client.post("/tasks", json={"title": "b"})
    titles = [t["title"] for t in client.get("/tasks").json()]
    assert titles == ["a", "b"]


def test_empty_title_is_rejected():
    r = client.post("/tasks", json={"title": "   "})
    assert r.status_code == 422


def test_delete_task():
    client.post("/tasks", json={"title": "temp"})
    assert client.delete("/tasks/1").status_code == 204
    assert client.get("/tasks").json() == []


def test_delete_unknown_task():
    assert client.delete("/tasks/999").status_code == 404
