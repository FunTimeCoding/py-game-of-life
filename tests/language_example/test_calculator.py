from py_game_of_life.language_example.calculator import Calculator


def test_add_numbers():
    calc = Calculator()
    assert calc.add(1, 2) == 3


def test_subtract_numbers():
    calc = Calculator()
    assert calc.subtract(1, 2) == -1
