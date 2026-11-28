# task-api-cicd

[![CI](https://github.com/Atemkeng23/task-api-cicd/actions/workflows/ci.yml/badge.svg)](https://github.com/Atemkeng23/task-api-cicd/actions/workflows/ci.yml)
[![Build Status](https://dev.azure.com/atemkengDevops/task-api-cicd/_apis/build/status%2FAtemkeng23.task-api-cicd?branchName=main)](https://dev.azure.com/atemkengDevops/task-api-cicd/_build/latest?definitionId=1&branchName=main)
![Python](https://img.shields.io/badge/python-3.11%20|%203.12-blue)
![License](https://img.shields.io/badge/license-MIT-green)

A small task API built with FastAPI. Every change goes through a CI pipeline before it counts.

## Why this project

I started out in QA automation, and I'm now moving into DevOps. This is the first project on that path. The app itself is kept simple on purpose: what I wanted to practice is everything around it. Each push runs the tests on two Python versions, and the test report is saved with the build.

Coming from testing, writing the tests first (TDD) felt natural, so that's how I built it.

## Status

| Item | State |
|---|---|
| FastAPI app (`/health`, `/tasks`) | Done |
| Automated tests (pytest, 7 tests) | Done |
| GitHub Actions CI (Python 3.11 and 3.12) | Done |
| Automated dependency updates (Dependabot) | Done |
| Azure DevOps pipeline | Done |
| Docker containerization | Planned (next project) |

## Prerequisites

- Python 3.11 or higher
- Git

## Quick start

```powershell
git clone https://github.com/Atemkeng23/task-api-cicd.git
cd task-api-cicd
python -m venv .venv
.venv\Scripts\Activate.ps1
pip install -r requirements.txt
uvicorn app.main:app --reload
```

The API listens on `http://127.0.0.1:8000`. Interactive documentation (Swagger UI) is available at `http://127.0.0.1:8000/docs`.

On Linux or macOS, activate the virtual environment with `source .venv/bin/activate`.

## Endpoints

| Method | Route | Description | Response |
|---|---|---|---|
| GET | `/health` | Check that the API is up | 200 |
| GET | `/tasks` | List tasks | 200 |
| POST | `/tasks` | Create a task (`{"title": "..."}`) | 201, or 422 if the title is empty |
| DELETE | `/tasks/{id}` | Delete a task | 204, or 404 if it does not exist |

For now, tasks live in memory, so they disappear when the server restarts. A real database comes in a later project.

## Running the tests

```powershell
pytest -v
```

The tests use FastAPI's `TestClient`. A fixture resets the state before each test, so no test depends on another.

## CI pipeline

The workflow `.github/workflows/ci.yml` runs on every push to `main` and on every pull request.

1. Check out the code (`actions/checkout`).
2. Set up Python with pip caching, as a matrix over versions 3.11 and 3.12.
3. Install dependencies.
4. Run pytest and generate a JUnit report (`report.xml`).
5. Upload the report as an artifact, even when tests fail (`if: always()`). A failing run is exactly when you want that report.

The first runs showed a Node 20 deprecation warning, so I updated the actions to versions that run on Node 24.

The same checks also run on Azure DevOps, defined in `azure-pipelines.yml`: a Microsoft-hosted Ubuntu agent, the same Python 3.11 and 3.12 matrix, and the JUnit report published to the Tests tab. Building the same pipeline twice was a good way to compare the two tools. A GitHub workflow and its jobs map to an Azure pipeline and its jobs, both use `matrix`, and `PublishTestResults` plays the role of the artifact upload.

## Repository structure

```text
.
├── app/
│   └── main.py              # FastAPI application
├── tests/
│   ├── test_health.py
│   └── test_tasks.py
├── .github/
│   └── workflows/
│       └── ci.yml           # CI pipeline
├── azure-pipelines.yml      # Azure DevOps pipeline
├── pytest.ini
├── requirements.txt
├── LICENSE
└── README.md
```

## What I learned

- Writing a test first, watching it fail, then writing just enough code to make it pass.
- Reading a failed pipeline run and its test report to find what broke.
- Keeping Git's local configuration separate from the global one.
- Creating a GitHub personal access token (PAT) with only the scopes it needs.

## License

Released under the MIT License, see [LICENSE](LICENSE).
