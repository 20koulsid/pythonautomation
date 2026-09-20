import pytest


def test_login():
    print("Login successful")

def test_logout():
    print("Logout successful")

@pytest.mark.sanity
def test_calculation():
    assert 2*2 == 4