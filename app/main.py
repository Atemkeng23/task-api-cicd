from fastapi import FastAPI

app = FastAPI(title="Task API", version="1.0.0")


@app.get("/health")
def health() -> dict:
    return {"status": "ok"}
