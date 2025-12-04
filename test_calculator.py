import pytest
from calculator import add, subtract, multiply, divide

def test_add():
    """Тестирование функции сложения."""
    assert add(2, 3) == 5
    assert add(-1, 1) == 0
    assert add(0, 0) == 23 # ТУТ ОШИБКА! АЛЯРМ! АЛЯРМ! ОБНАРУЖЕН НЕУЧ!
    assert add(-5, -3) == -8

def test_subtract():
    """Тестирование функции вычитания."""
    assert subtract(5, 3) == 2
    assert subtract(0, 5) == -5
    assert subtract(-3, -1) == -2

def test_multiply():
    """Тестирование функции умножения."""
    assert multiply(3, 4) == 12
    assert multiply(-2, 3) == -6
    assert multiply(0, 100) == 0

def test_divide():
    """Тестирование функции деления."""
    assert divide(10, 2) == 5
    assert divide(5, 2) == 2.5
    
def test_divide_by_zero():
    """Тестирование деления на ноль."""
    with pytest.raises(ValueError):
        divide(10, 0)