from numbers import Real


class CalculatorError(Exception):
    """Base exception for calculator errors."""
    pass


class InvalidInputError(CalculatorError, TypeError):
    """Invalid Input issuw"""
    pass


class DivisionByZeroError(CalculatorError, ZeroDivisionError):
    "Not diivisible by zero"
    pass


def _validate_numbers(a, b):
    # Reject booleans explicitly (since bool is subclass of int)
    if isinstance(a, bool) or isinstance(b, bool):
        raise InvalidInputError("Boolean values are not allowed.")

    if not isinstance(a, Real) or not isinstance(b, Real):
        raise InvalidInputError("Inputs must be real numbers (int or float).")


def add(a: float, b: float) -> float:
    """Addition function"""
    _validate_numbers(a, b)
    return a + b


def subtract(a: float, b: float) -> float:
    """Subtraction Function"""
    _validate_numbers(a, b)
    return a - b


def multiply(a: float, b: float) -> float:
    """Multiplication Function"""
    _validate_numbers(a, b)
    return a * b


def divide(a: float, b: float) -> float:
    """Division Functiom"""
    _validate_numbers(a, b)

    if b == 0:
        raise DivisionByZeroError("Division by zero is not allowed.")

    return a / b