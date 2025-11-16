"""
Tests for template endpoints.
"""
# flake8: noqa
# ruff: noqa
# type: ignore
{%- if cookiecutter.use_templates == 'y' %}
from fastapi import status


class TestTemplates:
    """Tests for template endpoints."""

    def test_home_page_success(self, client):
        """Test successful home page rendering."""
        response = client.get("/api/v1/")

        assert response.status_code == status.HTTP_200_OK
        assert "text/html" in response.headers["content-type"]
        assert "Welcome to" in response.text
        assert "{{ cookiecutter.project_name }}" in response.text or "FastAPI Template" in response.text

    def test_static_files_accessible(self, client):
        """Test that static files are accessible."""
        response = client.get("/static/styles.css")

        assert response.status_code == status.HTTP_200_OK
        assert "text/css" in response.headers["content-type"]
        assert "body" in response.text
{%- else %}
# Template tests are disabled when use_templates is 'n'
{%- endif %}
