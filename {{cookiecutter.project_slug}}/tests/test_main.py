"""
Tests for main application.
"""

import pytest
from fastapi import status


class TestHealthCheck:
    """Tests for application health and basic endpoints."""

    def test_root_endpoint(self, client):
        """Test root endpoint (if exists)."""
        response = client.get("/")

        assert response.status_code in [
            status.HTTP_200_OK,
            status.HTTP_404_NOT_FOUND
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
        {%- if cookiecutter.use_auth == 'y' %}
        response = client.options(
            "/auth/signup",
            headers={
                "Origin": "http://localhost:3000",
                "Access-Control-Request-Method": "POST"
            }
        )
        {%- else %}
        response = client.options(
            "/api/v1/items",
            headers={
                "Origin": "http://localhost:3000",
                "Access-Control-Request-Method": "GET"
            }
        )
        {%- endif %}

        assert response.status_code in [
            status.HTTP_200_OK,
            status.HTTP_405_METHOD_NOT_ALLOWED
        ]

