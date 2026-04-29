from operations import add, subtract, multiply, divide
from utils.input_handler import get_choice, get_number
from history.manager import add_entry, show_history, clear_history

def handle_result(num1: float, num2: float, symbol: str, result: float):
    entry: str = f"{num1} {symbol} {num2} = {result}"
    add_entry(entry)
    print('Result:', result)
    print()

def main():
    current_result: float | None = None

    while True:
        print('Select operation:')
        print('1. Add')
        print('2. Subtract')
        print('3. Multiply')
        print('4. Divide')
        print('5. Exit')
        print('6. Show History')
        print('7. Clear History')

        choice: int = get_choice('Enter your choice: ')

        if choice not in range(1, 8):
            print('Please choose valid options!')
            print()
            continue

        if choice == 5:
            print('Goodbye!')
            break

        if choice == 6:
            show_history()
            print()
            continue

        if choice == 7:
            clear_history()
            print()
            continue

        if current_result is None:
            num1: float = get_number('Enter your first number: ')
        else:
            print(f"Current result: {current_result}")
            while True:
                use_prev: str = input('Continue with this result? (y/n): ').lower()

                if use_prev == 'y':
                    num1 = current_result
                    break
                elif use_prev == 'n':
                    current_result = None
                    num1 = get_number('Enter your first number: ')
                    break
                else:
                    print("Please enter either 'y' or 'n'...")                

        num2: float = get_number('Enter your second number: ')

        

        if choice == 1:
            result: float = add(num1, num2)
            current_result = result
            handle_result(num1, num2, '+', result)
        elif choice == 2:
            result: float = subtract(num1, num2)
            current_result = result
            handle_result(num1, num2, '-', result)
        elif choice == 3:
            result: float = multiply(num1, num2)
            current_result = result
            handle_result(num1, num2, '*', result)
        elif choice == 4:
            try:
                result = divide(num1, num2)
                current_result = result
                handle_result(num1, num2, '/', result)
            except ValueError as e:
                print(e)
                print()


if __name__ == '__main__':
    main()