import pytest

def test_login():
    print("Login successful")

@pytest.mark.sanity
def test_logout():
    print("Logout successful")

@pytest.mark.skip
def test_calculation1():
    assert 2*2 == 4

@pytest.mark.xfail
def test_calculation2():
    assert 2-2 == 8