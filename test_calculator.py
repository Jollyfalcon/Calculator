import pytest
from Calculator import calculator_main

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
    ("3/0", ("3/0", "ERROR: Division by Zero.")),
    ("2++3", ("2++3", "ERROR: Consecutive operators.")),
    ("(2+3", ("(2+3", "ERROR: Unequal parenthesis.")),
    ("2+abc3", ("2+abc3", 'ERROR: Unexpected characters.')),
    ("--2--3", ("--2--3", "ERROR: Invalid operator at start or end.")),
    (")2+3(", (")5(", "ERROR: Inproperly paired parenthesis.")),
])
def test_valid_expressions(expression, expected):
    assert calculator_main(expression) == expected

def test_merge_negatives():
    # Test negative number handling
    assert calculator_main("-5") == ("-5","")
    assert calculator_main("3--2") == ("5","")
    assert calculator_main("-3*-2") == ("6","")
    assert calculator_main("5+-3") == ("2","")