import pytest

@pytest.fixture(scope="function",autouse=True)
def setUp():
    print("Launch browser")
    print("Login successful")
    print("Browse setup")
    yield
    print("Logoff successful")
    print("close browser")