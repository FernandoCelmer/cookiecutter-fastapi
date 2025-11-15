# cookiecutter-fastapi

![GitHub forks](https://img.shields.io/github/forks/FernandoCelmer/cookiecutter-fastapi?label=Forks&style=flat-square)
![GitHub Repo stars](https://img.shields.io/github/stars/FernandoCelmer/cookiecutter-fastapi?label=Stars&style=flat-square)
![GitHub last commit](https://img.shields.io/github/last-commit/FernandoCelmer/cookiecutter-fastapi?style=flat-square)

- **Documentation**: [https://fernandocelmer.github.io/cookiecutter-fastapi](https://fernandocelmer.github.io/cookiecutter-fastapi)
- **Source Code**: [https://github.com/FernandoCelmer/cookiecutter-fastapi](https://github.com/FernandoCelmer/cookiecutter-fastapi)


## Features

- [x] For FastAPI 0.104.1
- [x] Works with Python 3.12
- [x] Config for Serverless
- [x] Config for MySQL/SQLite
- [x] Docker & Docker Compose
- [x] Async/Sync support
- [x] UUID/Integer ID types
- [x] Mkdocs
- [x] Basic Auth JWT
- [x] Comprehensive test suite (pytest)
- [ ] Templates
- [ ] Crud

## Usage

First install cookiecutter

    pip install cookiecutter

Now run this command to clone

    cookiecutter https://github.com/FernandoCelmer/cookiecutter-fastapi

Now just fill in some information for the cookiecutter to do its work and replace it in the project.

    [1/18] repo_name (cookiecutter-fastapi): cookiecutter-fastapi
    [2/18] project_name (FastAPI Template): Test FastAPI 
    [3/18] project_slug (test_fastapi): 
    [4/18] description (Amazing project with FastAPI!): Amazing API
    [5/18] author_name (Fernando Celmer): Fernando Celmer
    [6/18] domain_name (fernandocelmer.com): fernandocelmer.com
    [7/18] email (fernando-celmer@fernandocelmer.com): email@fernandocelmer.com
    [8/18] version (0.1.0): 
    [9/18] Select open_source_license
        1 - MIT
        2 - BSD
        3 - Apache Software License 2.0
        4 - Not open source
        Choose from [1/2/3/4] (1): 1
    [10/18] Select id_type
        1 - UUID
        2 - Integer
        Choose from [1/2] (1): 1
    [11/18] url_documentation (#): 
    [12/18] url_source_code (#): 
    [13/18] use_async (y): 
    [14/18] use_mkdocs (y): 
    [15/18] use_serverless (y): 
    [16/18] use_templates (y): 
    [17/18] use_auth (y):
    [18/18] github_action_code_scan (y):

## Development

### Running with Docker

The template includes Docker and Docker Compose configuration for easy development setup.

1. Create a `.env` file based on `.env-exemple`:

    ```bash
    cp .env-exemple .env
    ```

2. Start the services:

    ```bash
    docker-compose up -d
    ```

3. The API will be available at `http://localhost:8000`
4. API documentation (Swagger UI) at `http://localhost:8000/docs`

### Running Tests

The template includes a comprehensive test suite using pytest.

1. Install dependencies:

    ```bash
    poetry install
    ```

2. Run tests:

    ```bash
    pytest
    ```

3. Run tests with coverage:

    ```bash
    pytest --cov=app --cov-report=html
    ```

### Commit Style

- ⚙️ FEATURE
- 📝 PEP8
- 📌 ISSUE
- 🪲 BUG
- 📘 DOCS
- 📦 PyPI
- ❤️️ TEST
- ⬆️ CI/CD
- ⚠️ SECURITY

### License

This project is licensed under the terms of the **MIT** license.
