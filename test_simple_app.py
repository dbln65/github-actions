# test_simple_app.py
from simple_app import square, cube

def test_square():
    assert square(2) == 4
    assert square(3) == 9
    assert square(4) == 16

def test_cube():
    assert cube(2) == 8
    assert cube(3) == 27
    assert cube(4) == 64

