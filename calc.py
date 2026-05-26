def _validate_numbers(a, b):
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("Both inputs must be numbers (int or float).")


def add(a: int, b: int) -> int:
    _validate_numbers(a, b)
    return a + b


def subtract(a: int, b: int) -> int:
    _validate_numbers(a, b)
    return a - b


def multiply(a: int, b: int) -> int:
    _validate_numbers(a, b)
    return a * b


def divide(a: int, b: int) -> float:
    _validate_numbers(a, b)

    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero.")

    return a / b