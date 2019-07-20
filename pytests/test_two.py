def fun():
    return True

def equals(x,y):
    return x+y

def test_find_true():
    assert fun() == True
    
def test_just_check():
    assert equals(5,6) == 11
