def get_choice(prompt: str) -> int:
    '''Receive prompt as an input and yield an integer as an output'''
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print('Please enter a valid integer choice.')

def get_number(prompt: str) -> float:
    '''Receive prompt as an input and yield a number as an output'''
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print('Invalid input. Please enter a number.')