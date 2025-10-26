import pytest
from calculadora import sumar, restar, multiplicar

def test_sumar():
    assert sumar(2, 3) == 5
    assert sumar(-1, 1) == 0

def test_restar():
    assert restar(5, 3) == 2
    assert restar(0, 5) == -5

def test_multiplicar():
    assert multiplicar(4, 3) == 12
    assert multiplicar(0, 10) == 0
```

**requirements.txt**:
```
pytest==7.4.3
pytest-cov==4.1.0
