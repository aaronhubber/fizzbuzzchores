def fizz_buzz(value):
    if value == 0:
        return str(value)
    elif value%3 == 0 and value%5 == 0:
        return "fizzbuzz"
    elif value%3 == 0:
        return "fizz"
    elif value%5 == 0:
        return "buzz"
    else:
        return str(value)
    
    