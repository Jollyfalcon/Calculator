import pytest
from Calculator import calculator_main

@pytest.mark.parametrize("expression, expected", [
    # Basic operations
    ("3+5", 8),
    ("10-4", 6),
    ("6*7", 42),
    ("20/5", 4),
    ("2^3", 8),
    
    # Operator precedence
    ("2+3*4", 14),
    ("(2+3)*4", 20),
    ("3*4^2", 48),
    ("3^2*4", 36),
    
    # Negative numbers
    ("-5+3", -2),
    ("3*-2", -6),
    ("-2^3", -8),
    ("(-2)^3", -8),
    ("-2--3", 1),
    
    # Complex parentheses
    ("2*(3+(4-1)*2)", 18),
    ("(2+3)*(4-1)", 15),
    ("((2+3)*4)^2", 400),
    
    # Division cases
    ("10/3", pytest.approx(3.333333, 0.0001)),
    ("0/5", 0),
])
def test_valid_expressions(expression, expected):
    assert calculator_main(expression) == expected

@pytest.mark.parametrize("expression, error_msg", [
    ("3/0", "ERROR: Division by Zero"),
    ("2++3", "ERROR: Consecutive operators"),
    ("(2+3", "ERROR: unequal parenthesis"),
    ("abc", "WARNING: Unexpected character"),
    ("--2--3", "ERROR: Operator at beginning or end"),
])
def test_error_cases(expression, error_msg, capsys):
    calculator_main(expression)
    captured = capsys.readouterr()
    assert error_msg in captured.out

def test_merge_negatives():
    # Test negative number handling
    assert calculator_main("-5") == -5
    assert calculator_main("3--2") == 5
    assert calculator_main("-3*-2") == 6
    assert calculator_main("5+-3") == 2