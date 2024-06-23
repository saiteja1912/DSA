def divide(a, b):
    assert b != 0, "Zero Division Error"
    return a/b

def test_division():
    assert divide(2, 1) == 2
    print(f'** 1st test passed **\n')
    assert divide(4, 2) == 2
    print(f'** 2nd test passed **')
test_division()