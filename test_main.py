""" Test Main.py """

from main import hello_world


def test_main():
    """Assert hello_world() returns
    Hola Mundo
    """
    assert hello_world() == "Hola Mundo"
