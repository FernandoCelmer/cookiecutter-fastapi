# {{ cookiecutter.project_name }}

{{ cookiecutter.description }}

- **Documentation**: [{{ cookiecutter.url_documentation }}]({{ cookiecutter.url_documentation }})
- **Source Code**: [{{ cookiecutter.url_source_code }}]({{ cookiecutter.url_source_code }})

## Development

### Running with Docker

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

### Code Quality

1. Install code quality dependencies:

    ```bash
    poetry install --with code-quality
    ```

2. Run code quality checks:

    ```bash
    # Run Ruff (linting and formatting)
    poetry run ruff check --config=.code_quality/ruff.toml app/ tests/
    poetry run ruff format --check --config=.code_quality/ruff.toml app/ tests/

    # Run Flake8
    poetry run flake8 --append-config=.code_quality/.flake8 app/ tests/

    # Run MyPy (type checking)
    poetry run mypy --config-file=.code_quality/mypy.ini app/
    ```

3. Setup pre-commit hooks:

    ```bash
    poetry run pre-commit install
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

This project is licensed under the terms of the {{ cookiecutter.open_source_license }} license.
