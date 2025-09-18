# robust_division_calculator.py

def safe_divide(numerator, denominator):
    """
    Perform safe division handling non-numeric input and division by zero.
    Returns a string with the result or an error message.
    """
    try:
        num = float(numerator)
        den = float(denominator)
    except ValueError:
        return "Error: Please enter numeric values only."

    try:
        result = num / den
        return f"The result of the division is {result}"
    except ZeroDivisionError:
        return "Error: Cannot divide by zero."
