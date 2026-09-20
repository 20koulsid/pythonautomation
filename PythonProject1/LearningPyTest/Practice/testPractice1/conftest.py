import pytest


@pytest.fixture(autouse=True)
def setup():
    print("setup")