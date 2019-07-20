import pytest
import random

#@pytest.mark.customtest
def test_send_data():
    pass

def power(x):
    value = x ** random.randint(1,8)
    print(f"Random value : {value}")

def fun(x):
    return x+1

def test_answer():
    assert fun(5) == 6

def test_modulo():
    value = power(5)
    print(f"Value of x: {value}")
    #assert value %2 == 0, "Value was odd, should be even "
    pass