Token = str | float

def evaluate(tokens: list[Token]) -> float:
    tokens = tokens[:]

    if len(tokens) % 2 == 0:
        raise ValueError('Malformed expression')

    # handle * and /
    i: int = 0
    while i < len(tokens):
        if tokens[i] == '*':
            result: float = tokens[i - 1] * tokens[i + 1]
            tokens[i-1:i+2] = [result]
            i -= 1
        elif tokens[i] == '/':
            if tokens[i + 1] == 0:
                raise ValueError('Cannot divide by zero')
            result: float = tokens[i - 1] / tokens[i + 1]
            tokens[i-1:i+2] = [result]
            i -= 1
        else:
            i += 1

    # handle + and -
    result: float = tokens[0]
    
    j: int = 1
    while j < len(tokens):
        operator = tokens[j]
        next_number = tokens[j + 1]

        if operator == '+':
            result += next_number
        elif operator == '-':
            result -= next_number

        j += 2

    return result