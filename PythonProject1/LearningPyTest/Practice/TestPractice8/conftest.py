import pytest

@pytest.fixture(scope="module", autouse=True)
def setup():
    print("setup1")
    print("setup2")
    print("setup3")
    print("setup4")
    print("setup5")
    yield
    print("teardown1")
    print("teardown2")