import numbers

def _validate_numbers(a, b):
    if not isinstance(a, numbers.Real) or not isinstance(b, numbers.Real):
        raise TypeError("Inputs must be real numbers (int or float).")


def add(a: float, b: float) -> float:
    _validate_numbers(a, b)
    return a + b


def subtract(a: float, b: float) -> float:
    _validate_numbers(a, b)
    return a - b


def multiply(a: float, b: float) -> float:
    _validate_numbers(a, b)
    return a * b


def divide(a: float, b: float) -> float:
    _validate_numbers(a, b)

    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero.")

    return a / b