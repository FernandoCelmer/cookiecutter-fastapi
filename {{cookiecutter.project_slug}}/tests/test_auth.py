"""
Tests for authentication endpoints.
"""
# flake8: noqa
# ruff: noqa
# type: ignore
{%- if cookiecutter.use_auth == 'y' %}
from fastapi import status


class TestSignup:
    """Tests for signup endpoint."""

    def test_signup_success(self, client, test_user_data):
        """Test successful user signup."""
        response = client.post("/auth/signup", json=test_user_data)

        assert response.status_code == status.HTTP_200_OK
        data = response.json()
        assert data["email"] == test_user_data["email"]
        assert data["username"] == test_user_data["username"]
        assert "password" not in data

    def test_signup_duplicate_email(self, client, test_user_data):
        """Test signup with duplicate email."""
        client.post("/auth/signup", json=test_user_data)
        response = client.post("/auth/signup", json=test_user_data)

        assert response.status_code == status.HTTP_422_UNPROCESSABLE_ENTITY
        assert "Account already exists" in response.json()["detail"]

    def test_signup_invalid_email(self, client):
        """Test signup with invalid email format."""
        invalid_data = {
            "email": "invalid-email",
            "username": "testuser",
            "password": "testpassword123",
        }
        response = client.post("/auth/signup", json=invalid_data)

        assert response.status_code == status.HTTP_422_UNPROCESSABLE_ENTITY

    def test_signup_missing_fields(self, client):
        """Test signup with missing required fields."""
        incomplete_data = {"email": "test@example.com"}
        response = client.post("/auth/signup", json=incomplete_data)

        assert response.status_code == status.HTTP_422_UNPROCESSABLE_ENTITY


class TestLogin:
    """Tests for login endpoint."""

    def test_login_success(self, client, test_user_data):
        """Test successful login."""
        client.post("/auth/signup", json=test_user_data)

        response = client.post(
            "/auth/login",
            json={
                "email": test_user_data["email"],
                "password": test_user_data["password"],
            },
        )

        assert response.status_code == status.HTTP_200_OK
        data = response.json()

        assert "access_token" in data
        assert "refresh_token" in data
        assert isinstance(data["access_token"], str)
        assert isinstance(data["refresh_token"], str)

    def test_login_invalid_email(self, client):
        """Test login with non-existent email."""
        response = client.post(
            "/auth/login",
            json={
                "email": "nonexistent@example.com",
                "password": "password123",
            },
        )

        assert response.status_code == status.HTTP_401_UNAUTHORIZED
        assert "Invalid email" in response.json()["detail"]

    def test_login_invalid_password(self, client, test_user_data):
        """Test login with wrong password."""
        client.post("/auth/signup", json=test_user_data)
        response = client.post(
            "/auth/login",
            json={
                "email": test_user_data["email"],
                "password": "wrongpassword",
            },
        )

        assert response.status_code == status.HTTP_401_UNAUTHORIZED
        assert "Invalid password" in response.json()["detail"]

    def test_login_missing_fields(self, client):
        """Test login with missing fields."""
        response = client.post(
            "/auth/login", json={"email": "test@example.com"}
        )

        assert response.status_code == status.HTTP_422_UNPROCESSABLE_ENTITY


class TestRefreshToken:
    """Tests for refresh token endpoint."""

    def test_refresh_token_success(self, client, refresh_token):
        """Test successful token refresh."""
        response = client.get(
            "/auth/refresh_token",
            headers={"Authorization": f"Bearer {refresh_token}"},
        )

        assert response.status_code == status.HTTP_200_OK
        data = response.json()
        assert "access_token" in data
        assert isinstance(data["access_token"], str)

    def test_refresh_token_missing_auth(self, client):
        """Test refresh token without authorization header."""
        response = client.get("/auth/refresh_token")

        assert response.status_code == status.HTTP_403_FORBIDDEN

    def test_refresh_token_invalid_token(self, client):
        """Test refresh token with invalid token."""
        response = client.get(
            "/auth/refresh_token",
            headers={"Authorization": "Bearer invalid_token"},
        )

        assert response.status_code == status.HTTP_401_UNAUTHORIZED

    def test_refresh_token_with_access_token(self, client, auth_headers):
        """Test refresh token endpoint with access token (should fail)."""
        access_token = auth_headers["Authorization"].split(" ")[1]
        response = client.get(
            "/auth/refresh_token",
            headers={"Authorization": f"Bearer {access_token}"},
        )
        assert response.status_code == status.HTTP_401_UNAUTHORIZED
{%- else %}
{%- endif %}