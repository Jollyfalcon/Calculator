import pytest
from Calculator import Calculator

calculator = Calculator()

@pytest.mark.parametrize("expression, expected", [
    # Basic operations
    ("3+5", ('8','')),
    ("10-4", ('6','')),
    ("6*7", ('42','')),
    ("21/5", ('4.2','')),
    ("2^3", ('8','')),
    
    # Operator precedence
    ("2+3*4", ('14','')),
    ("(2+3)*4", ('20','')),
    ("3*4^2", ('48','')),
    ("3^2*4", ('36','')),
    
    # Negative numbers
    ("-5+3", ('-2','')),
    ("3*-2", ('-6','')),
    ("-2^3", ('-8','')),
    ("(-2)^3", ('-8','')),
    ("-2--3", ('1','')),
    
    # Complex parentheses
    ("2*(3+(4-1)*2)", ('18','')),
    ("(2+3)*(4-1)", ('15','')),
    ("((2+3)*4)^2", ('400','')),
    
    # Division cases
    ("10/3", ('3.3333333333333335', '')),
    ("0/5", ("0","")),

    #Error messages
    ("", ("", "Invalid: No expression")),
    ("3/0", ("3/0", "Error: Division by zero")),
    ("2++3", ("2++3", "Invalid: Consecutive operators")),
    ("(2+3", ("(2+3", "Invalid: Unbalanced parentheses")),
    ("2+5abc3", ("2+5abc3", 'Invalid: Unexpected characters')),
    ("--2--3", ("--2--3", "Invalid: Operators at start/end")),
    (")2+3(", (")2+3(", "Invalid: Improperly paired parenthesis")),
    ("8..3+5", ("8..3+5", "Invalid: Consecutive numbers")),
    ("8(3+5)", ("8(3+5)", "Error: Calculation incomplete")),
    ("8...3+5", ("8...3+5", "Invalid: Excess decimal points")),
])
def test_valid_expressions(expression, expected):
    assert calculator.calculate(expression) == expected

def test_merge_negatives():
    # Test negative number handling
    assert calculator.calculate("-5") == ("-5","")
    assert calculator.calculate("3--2") == ("5","")
    assert calculator.calculate("-3*-2") == ("6","")
    assert calculator.calculate("5+-3") == ("2","")