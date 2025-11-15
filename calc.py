class Calculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if b == 0:
            raise ValueError("Cannot divide by zero.")
        return a / b


def main():
    calc = Calculator()
    print("Simple Python Calculator")
    while True:
        try:
            num1 = float(input("Enter first number (or 'q' to quit): "))
        except ValueError:
            print("Exiting calculator.")
            break

        try:
            num2 = float(input("Enter second number: "))
        except ValueError:
            print("Invalid input for second number. Please try again.")
            continue

        print("Select operation:")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")

        choice = input("Enter choice (1/2/3/4): ")

        try:
            if choice == '1':
                result = calc.add(num1, num2)
            elif choice == '2':
                result = calc.subtract(num1, num2)
            elif choice == '3':
                result = calc.multiply(num1, num2)
            elif choice == '4':
                result = calc.divide(num1, num2)
            else:
                print("Invalid choice. Please select a valid operation.")
                continue
            print(f"Result: {result}")
        except ValueError as e:
            print(e)

        print()  # Blank line for readability


if __name__ == "__main__":
    main()
