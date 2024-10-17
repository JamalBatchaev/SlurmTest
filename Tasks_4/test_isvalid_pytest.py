from  isvalid import is_valid

def test_is_valid():
    assert is_valid('()')
    assert is_valid('{}')
    assert is_valid('[]')

def test_is_not_valid():
    assert not is_valid('())')
    assert not is_valid('{[}]')
    assert not is_valid('[')