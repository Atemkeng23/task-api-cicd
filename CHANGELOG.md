# Changelog

All notable changes to this project are documented here.
The format follows [Keep a Changelog](https://keepachangelog.com/en/1.1.0/).

## [Unreleased]

### Added
- Dependabot configuration for pip and GitHub Actions.
- CONTRIBUTING and SECURITY documents.
- Azure DevOps pipeline (`azure-pipelines.yml`) running the tests on Python 3.11 and 3.12.
- Branch protection on `main`: pull request and green checks required.

## [1.0.0] - 2026-11-27

### Added
- FastAPI application with `/health` and `/tasks` endpoints.
- Automated tests with pytest.
- GitHub Actions CI on Python 3.11 and 3.12, with test report artifact.
- Project README.
