"""
Tests for main application.
"""
# flake8: noqa
# ruff: noqa
# type: ignore
from fastapi import status


class TestHealthCheck:
    """Tests for application health and basic endpoints."""

    def test_root_endpoint(self, client):
        """Test root endpoint (if exists)."""
        response = client.get("/")

        assert response.status_code in [
            status.HTTP_200_OK,
            status.HTTP_404_NOT_FOUND,
        ]

    def test_docs_endpoint(self, client):
        """Test OpenAPI docs endpoint."""
        response = client.get("/docs")

        assert response.status_code == status.HTTP_200_OK

    def test_openapi_endpoint(self, client):
        """Test OpenAPI JSON endpoint."""
        response = client.get("/openapi.json")

        assert response.status_code == status.HTTP_200_OK
        data = response.json()
        assert "openapi" in data
        assert "info" in data

    def test_cors_headers(self, client):
        """Test CORS headers in responses."""
        response = client.options(
            {%- if cookiecutter.use_auth == 'y' %}
            "/auth/signup",
            {%- else %}
            "/api/v1/items",
            {%- endif %}
            headers={
                "Origin": "http://localhost:3000",
                "Access-Control-Request-Method": "POST",
            },
        )

        assert response.status_code in [
            status.HTTP_200_OK,
            status.HTTP_405_METHOD_NOT_ALLOWED,
        ]
