Token = str | float

def validate_tokens(tokens: list[Token]) -> None:
    if not tokens:
        raise ValueError('Empty expression')
    
    # Must start and end with a number
    if not isinstance(tokens[0], float) or not isinstance(tokens[-1], float):
        raise ValueError('Expression must start and end with a number')
    
    # No two operators in a row
    for i in range(len(tokens) - 1):
        if isinstance(tokens[i], str) == isinstance(tokens[i+1], str):
            raise ValueError('Invalid expression structure')