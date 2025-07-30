import pytest
from Calculator import calculator_main

@pytest.mark.parametrize("expression, expected", [
    # Basic operations
    ("3+5", ('8.0','')),
    ("10-4", ('6.0','')),
    ("6*7", ('42.0','')),
    ("20/5", ('4.0','')),
    ("2^3", ('8.0','')),
    
    # Operator precedence
    ("2+3*4", ('14.0','')),
    ("(2+3)*4", ('20.0','')),
    ("3*4^2", ('48.0','')),
    ("3^2*4", ('36.0','')),
    
    # Negative numbers
    ("-5+3", ('-2.0','')),
    ("3*-2", ('-6.0','')),
    ("-2^3", ('-8.0','')),
    ("(-2)^3", ('-8.0','')),
    ("-2--3", ('1.0','')),
    
    # Complex parentheses
    ("2*(3+(4-1)*2)", ('18.0','')),
    ("(2+3)*(4-1)", ('15.0','')),
    ("((2+3)*4)^2", ('400.0','')),
    
    # Division cases
    ("10/3", ('3.3333333333333335', '')),
    ("0/5", ("0.0","")),

    #Error messages
    ("3/0", ("3.0/0.0", "ERROR: Division by Zero.")),
    ("2++3", ("2.0++3.0", "ERROR: Consecutive operators.")),
    ("(2+3", ("(2.0+3.0", "ERROR: Unequal parenthesis.")),
    ("2+abc3", ("5.0", "WARNING: Unexpected character, calculation may be incorrect.")),
    ("--2--3", ("--2.0--3.0", "ERROR: Invalid operator at start or end.")),
])
def test_valid_expressions(expression, expected):
    assert calculator_main(expression) == expected

# @pytest.mark.parametrize("expression, error_msg", [
#     ("3/0", ("3.0/0.0", "ERROR: Division by Zero")),
#     ("2++3", ("2.0++3.0", "ERROR: Consecutive operators")),
#     ("(2+3", ("(2.0+3.0)", "ERROR: unequal parenthesis")),
#     ("abc", ("abc", "WARNING: Unexpected character")),
#     ("--2--3", ("--2--3", "ERROR: Operator at beginning or end")),
# ])
# def test_error_cases(expression, error_msg, capsys):
#     calculator_main(expression)
#     captured = capsys.readouterr()
#     assert error_msg in captured.out

def test_merge_negatives():
    # Test negative number handling
    assert calculator_main("-5") == ("-5.0","")
    assert calculator_main("3--2") == ("5.0","")
    assert calculator_main("-3*-2") == ("6.0","")
    assert calculator_main("5+-3") == ("2.0","")