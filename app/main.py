from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI(title="Task API", version="1.0.0")

# In-memory storage for now. A database is added in a later project.
_tasks: dict[int, dict] = {}
_next_id = 1


class TaskIn(BaseModel):
    title: str


@app.get("/health")
def health() -> dict:
    return {"status": "ok"}


@app.get("/tasks")
def list_tasks() -> list[dict]:
    return list(_tasks.values())


@app.post("/tasks", status_code=201)
def create_task(task: TaskIn) -> dict:
    global _next_id
    if not task.title.strip():
        raise HTTPException(status_code=422, detail="title must not be empty")
    item = {"id": _next_id, "title": task.title.strip()}
    _tasks[_next_id] = item
    _next_id += 1
    return item


@app.delete("/tasks/{task_id}", status_code=204)
def delete_task(task_id: int) -> None:
    if task_id not in _tasks:
        raise HTTPException(status_code=404, detail="task not found")
    del _tasks[task_id]
