Token = str | float

def flush_number(tokens: list[Token], current_number: str) -> None:
    if current_number:
        if not any(c.isdigit() for c in current_number):
            raise ValueError('Invalid number format')
        tokens.append(float(current_number))

def tokenize(expression: str) -> list[Token]:
    tokens: list[Token] = []
    current_number: str = ''
    dot_used: bool = False

    for char in expression:
        if char.isdigit():
            current_number += char
        elif char == '.':
            if dot_used:
                raise ValueError('Invalid number format')
            dot_used = True
            current_number += char
        elif char in '+-*/':
            if current_number:
                flush_number(tokens, current_number)
                current_number = ''
                dot_used = False
            tokens.append(char)
        elif char == ' ':
            continue
        else:
            raise ValueError(f'Invalid character: {char}')
        
    if current_number:
        flush_number(tokens, current_number)

    return tokens