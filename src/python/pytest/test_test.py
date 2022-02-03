import pytest

@pytest.mark.parametrize("number", [1, 2, 3, 4, 42])
def test_foo(number):
    assert number > 0 