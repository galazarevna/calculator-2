"""Functions for common math operations."""
 

def add(a_list):
    """Return the sum of the two input integers."""
    output = float(a_list[1])
    for i in range(2, len(a_list)):
        output += float(a_list[i])
    return output


def subtract(a_list):
    """Return the second number subtracted from the first."""
    output = float(a_list[1])
    for i in range(2, len(a_list)):
        output -= float(a_list[i])
    return output


def multiply(a_list):
    """Multiply the two inputs together."""
    output = float(a_list[1])
    for i in range(2, len(a_list)):
        output *= float(a_list[i])
    return output


def divide(a_list):
    """Divide the first input by the second, returning a floating point."""
    output = float(a_list[1])
    for i in range(2, len(a_list)):
        output /= float(a_list[i])
    return output


def square(a_list):
    """Return the square of the input."""
    return float(a_list[1]) ** 2


def cube(a_list):
    """Return the cube of the input."""
    return float(a_list[1]) ** 3


def power(a_list):
    """Raise num1 to the power of num and return the value."""
    output = float(a_list[1])
    for i in range(2, len(a_list)):
        output = output ** float(a_list[i])
    return output


def mod(a_list):
    """Return the remainder of num1 / num2."""

    return float(a_list[1]) % float(a_list[2])
