def tryConvertToInt(value):
    try:
        return int(value)  # If conversion is a success, return the integer
    except ValueError:
        return False