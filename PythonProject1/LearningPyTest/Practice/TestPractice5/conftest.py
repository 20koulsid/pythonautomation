import pytest

@pytest.fixture
def login_data():
    return {
        "username": "admin",
        "password": "admin123"
    }