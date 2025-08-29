import pytest
from Calculator import Calculator

# Initialize calculator instance for testing
calculator = Calculator()

def test_basic_arithmetic_operations() -> None:
    """
    Test basic arithmetic operations: addition, subtraction, 
    multiplication, division, and exponentiation.
    """
    basic_operations = [
        ("3+5",4, ('8','')),
        ("10-4",4, ('6','')),
        ("6*7",4, ('42','')),
        ("21/5",4, ('4.2','')),
        ("2^3",4, ('8','')),
    ]
    
    for expression, decimal, expected in basic_operations:
        result = calculator.calculate(expression, decimal)
        assert result == expected, f"Failed floating point test: {expression}, {decimal}"

def test_operator_precedence() -> None:
    """
    Verify correct order of operations (PEMDAS) 
    and handling of operator precedence.
    """
    precedence_tests = [
        ("2+3*4",4, ('14','')),
        ("(2+3)*4",4, ('20','')),
        ("3*4^2",4, ('48','')),
        ("3^2*4",4, ('36','')),
    ]
    
    for expression, decimal, expected in precedence_tests:
        result = calculator.calculate(expression, decimal)
        assert result == expected, f"Failed floating point test: {expression}, {decimal}"

def test_negative_number_expressions() -> None:
    """
    Test calculations involving negative numbers 
    in various contexts.
    """
    negative_number_tests = [
        ("-5+3",4, ('-2','')),
        ("3*-2",4, ('-6','')),
        ("-2^3",4, ('-8','')),
        ("(-2)^3",4, ('-8','')),
        ("-2--3",4, ('1','')),
        ("-5",4, ('-5','')),
        ("-3*-2",4, ("6","")),
    ]
    
    for expression, decimal, expected in negative_number_tests:
        result = calculator.calculate(expression, decimal)
        assert result == expected, f"Failed floating point test: {expression}, {decimal}"

def test_complex_parentheses() -> None:
    """
    Test nested and complex parenthetical expressions.
    """
    parentheses_tests = [
        ("2*(3+(4-1)*2)",4, ('18','')),
        ("(2+3)*(4-1)",4, ('15','')),
        ("((2+3)*4)^2",4, ('400','')),
    ]
    
    for expression, decimal, expected in parentheses_tests:
        result = calculator.calculate(expression, decimal)
        assert result == expected, f"Failed floating point test: {expression}, {decimal}"

def test_division_cases() -> None:
    """
    Test various division scenarios.
    """
    division_tests = [
        ("10/3",4, ('3.3333', '')),
        ("0/5",4, ("0","")),
    ]
    
    for expression, decimal, expected in division_tests:
        result = calculator.calculate(expression, decimal)
        assert result == expected, f"Failed floating point test: {expression}, {decimal}"

def test_error_handling() -> None:
    """
    Comprehensive test for various error scenarios 
    and invalid input handling.
    """
    error_tests = [
        #Error messages
        ("",4, ("", "Invalid: No expression")),
        ("3/0",4, ("3/0", "Error: Division by zero")),
        ("2++3",4, ("2++3", "Invalid: Consecutive operators")),
        ("(2+3",4, ("(2+3", "Invalid: Unbalanced parentheses")),
        ("2+5abc3",4, ("2+5abc3", 'Invalid: Unexpected characters')),
        ("--2--3",4, ("--2--3", "Invalid: Operators at start/end")),
        (")2+3(",4, (")2+3(", "Invalid: Improperly paired parenthesis")),
        ("8..3+5",4, ("8..3+5", "Invalid: Consecutive numbers")),
        ("8(3+5)",4, ("8(3+5)", "Error: Calculation incomplete")),
        ("8...3+5",4, ("8...3+5", "Invalid: Excess decimal points")),
        ("9^999999",4, ("9^999999", "Error: Overflow due to large numbers"))
    ]
    
    for expression, decimal, expected in error_tests:
        result = calculator.calculate(expression, decimal)
        assert result == expected, f"Failed floating point test: {expression}, {decimal}"

def test_float_display() -> None:
    """
    Test display of floating point at different
    selected number of decimals to display
    """

    floating_point_test = [
        ('3.141592',2,('3.14','')),
        ('3.141592',3,('3.142','')),
        ('3.141592',4,('3.1416','')),
        ('3.141592',5,('3.14159','')),
        ('3.141592',6,('3.141592','')),
        ('0.1+0.2',4,('0.3','')),
        ('5.04',4,('5.04','')),
        ('5.004',4,('5.004','')),
        ('5.0004',4,('5.0004','')),
        ('5.00004',4,('5','')),
    ]

    for expression, decimal, expected in floating_point_test:
        result = calculator.calculate(expression, decimal)
        assert result == expected, f"Failed floating point test: {expression}, {decimal}"
