class Calculator:
    def __init__(self):
        pass

    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def division(self, a, b):
        if b == 0:
            return "Zero Division Error"
        else:
            return a / b

    def multiplication(self, a, b):
        return a * b


# Create an instance of Calculator
calc = Calculator()

while True:
    print('Enter your choice:')
    print('1. Add')
    print('2. Subtract')
    print('3. Divide')
    print('4. Multiply')
    print('5. Exit')

    choice = int(input('Enter your choice: '))

    if choice == 5:
        print('Exiting the calculator')
        break
    else:
        num1 = float(input('Enter Num1: '))
        num2 = float(input('Enter Num2: '))

        if choice == 1:
            print(f'The result is: {calc.add(num1, num2)}')
        elif choice == 2:
            print(f'The result is: {calc.subtract(num1, num2)}')
        elif choice == 3:
            print(f'The result is: {calc.division(num1, num2)}')
        elif choice == 4:
            print(f'The result is: {calc.multiplication(num1, num2)}')
        else:
            print('Invalid choice, please try again.')
