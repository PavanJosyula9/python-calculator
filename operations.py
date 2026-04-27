def add(a: float, b: float) -> float:
    '''Add two numbers, and return a number as an output'''
    return a + b

def subtract(a: float, b: float) -> float:
    '''Subtract two numbers, and return a number as an output'''
    return a - b

def multiply(a: float, b: float) -> float:
    '''Multiply two numbers, and return a number as an output'''
    return a * b

def divide(a: float, b: float) -> float:
    '''Divide two numbers, 
    given b is not equal to zero, and 
    return a number as an output'''
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a/b