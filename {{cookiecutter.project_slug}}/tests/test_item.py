"""
Tests for item endpoints.
"""
# flake8: noqa
# ruff: noqa
# type: ignore
from uuid import uuid4

from fastapi import status


class TestItem:
    """Tests for item endpoint."""
    {%- if cookiecutter.use_auth == 'y' %}

    def test_get_items_success_with_auth(self, client, auth_headers):
        """Test successful items retrieval with authentication."""
        response = client.get("/api/v1/items", headers=auth_headers)

        assert response.status_code == status.HTTP_200_OK
        data = response.json()
        assert "resource" in data
        assert data["resource"] == "item"

    def test_get_item_by_id_success_with_auth(self, client, auth_headers):
        """Test successful item retrieval by ID with authentication."""
        test_id = uuid4()
        response = client.get(
            f"/api/v1/items/{test_id}",
            headers=auth_headers,
        )

        assert response.status_code == status.HTTP_200_OK
        data = response.json()
        assert "item_id" in data
        assert str(data["item_id"]) == str(test_id)

    def test_get_items_unauthorized(self, client):
        """Test items endpoint without authentication."""
        response = client.get("/api/v1/items")

        assert response.status_code == status.HTTP_403_FORBIDDEN

    def test_get_item_by_id_unauthorized(self, client):
        """Test item by ID endpoint without authentication."""
        test_id = uuid4()
        response = client.get(f"/api/v1/items/{test_id}")

        assert response.status_code == status.HTTP_403_FORBIDDEN

    def test_get_items_invalid_token(self, client):
        """Test items endpoint with invalid token."""
        response = client.get(
            "/api/v1/items",
            headers={"Authorization": "Bearer invalid_token"},
        )

        assert response.status_code == status.HTTP_401_UNAUTHORIZED

    def test_get_item_by_id_invalid_token(self, client):
        """Test item by ID endpoint with invalid token."""
        test_id = uuid4()
        response = client.get(
            f"/api/v1/items/{test_id}",
            headers={"Authorization": "Bearer invalid_token"},
        )

        assert response.status_code == status.HTTP_401_UNAUTHORIZED

    def test_get_items_expired_token(self, client):
        """Test items endpoint with expired token."""
        expired_token = "expired_token_placeholder"
        response = client.get(
            "/api/v1/items",
            headers={"Authorization": f"Bearer {expired_token}"},
        )

        assert response.status_code == status.HTTP_401_UNAUTHORIZED

    def test_get_item_by_id_expired_token(self, client):
        """Test item by ID endpoint with expired token."""
        test_id = uuid4()
        expired_token = "expired_token_placeholder"
        response = client.get(
            f"/api/v1/items/{test_id}",
            headers={"Authorization": f"Bearer {expired_token}"},
        )

        assert response.status_code == status.HTTP_401_UNAUTHORIZED
    {%- else %}
    def test_get_items_success(self, client):
        """Test successful items retrieval."""
        response = client.get("/api/v1/items")

        assert response.status_code == status.HTTP_200_OK
        data = response.json()
        assert "resource" in data
        assert data["resource"] == "item"

    def test_get_item_by_id_success(self, client):
        """Test successful item retrieval by ID."""
        test_id = uuid4()
        response = client.get(f"/api/v1/items/{test_id}")

        assert response.status_code == status.HTTP_200_OK
        data = response.json()
        assert "item_id" in data
        assert str(data["item_id"]) == str(test_id)
    {%- endif %}
