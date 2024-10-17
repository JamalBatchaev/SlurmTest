from  myRange import my_range

def test_is_valid():
    assert my_range(1.0)
    assert my_range(10.0, 5.0)
    assert my_range(50, 10, 2)  
