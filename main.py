from operations import add, subtract, multiply, divide

def main():
    while True:
        try:
            print('Select operation:')
            print('1. Add')
            print('2. Subtract')
            print('3. Multiply')
            print('4. Divide')
            print('5. Exit')

            choice: int = int(input("Enter your choice: "))

            if choice not in range(1,6):
                print('Please choose valid options!')
                continue

            if choice == 5:
                print('Goodbye!')
                break

            
            num1: float = float(input('Enter your first number: '))
            num2: float = float(input('Enter your second number: '))

            if choice == 1:
                print('Result:', add(num1, num2))
            elif choice == 2:
                print('Result:', subtract(num1, num2))
            elif choice == 3:
                print('Result:', multiply(num1, num2))
            elif choice == 4:
                try:
                    result = divide(num1, num2)
                    print('Result:', result)
                except ValueError as e:
                    print(e)
        except ValueError:
            print('Invalid input! Please enter numbers only.')


if __name__ == '__main__':
    main()