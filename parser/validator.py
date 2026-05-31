from parser.token_types import Token

OPERATORS = {'+', '-', '*', '/'}

def validate_tokens(tokens: list[Token]) -> None:
    if not tokens:
        raise ValueError('Empty expression')

    # Expression cannot start or end with an operator
    if tokens[0] in OPERATORS:
        raise ValueError('Expression cannot start with an operator')
    
    if tokens[-1] in OPERATORS:
        raise ValueError('Expression cannot end with an operator')

    for i in range(len(tokens) - 1):
        current: Token = tokens[i]
        next_token: Token = tokens[i+1]

        # Two operators in a row
        if current in OPERATORS and next_token in OPERATORS:
            raise ValueError('Invalid expression: consecutive operators')
        
        # Two numbers in a row
        if isinstance(current, float) and isinstance(next_token, float):
            raise ValueError('Invalid expression: consecutive numbers')
        
def validate_parentheses(tokens: list[Token]) -> None:
    balance = 0

    for token in tokens:
        if token == '(':
            balance += 1
        elif token == ')':
            balance -= 1

        if balance < 0: 
            raise ValueError('Mismatched Parentheses')
        
    if balance != 0:
        raise ValueError('Mismatched Parentheses')
    
def validate_expression(tokens: list[Token]) -> None:
    validate_parentheses(tokens)
    validate_tokens(tokens)
        