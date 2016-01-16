from py_game_of_life.py_game_of_life import PyGameOfLife


def test_return_code():
    application = PyGameOfLife()
    assert application.run() == 0
