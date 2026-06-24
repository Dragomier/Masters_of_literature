
def positive_int(value):
    try:
        value = int(value)
    except ValueError:
        raise ValueError("Value must be an integer")
    if value < 0:
        raise ValueError("Value must be positive")
    return value