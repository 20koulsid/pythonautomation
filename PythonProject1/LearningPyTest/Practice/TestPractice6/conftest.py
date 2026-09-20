import pytest

@pytest.fixture(autouse=True)
def love():
    print("love is in air")