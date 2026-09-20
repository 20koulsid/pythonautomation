import pytest

@pytest.fixture(scope="function", autouse=True)
def setup():
    print("username: test")
    print("password: test")
    print("author: test")
    print("street: test")