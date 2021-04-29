def add(a, b):
    return a + b


def sub(a, b):
    return a - b


def mult(a, b):
    return a * b


def div(a, b):

    # Check for divide by zero
    if b == 0:
        return float("nan")
    else:
        return a / b
