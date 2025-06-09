#Calculator with History

class Calculator:
    def __init__(self):
        self.history = []

    def add(self, a, b):
        result = a + b
        self.history.append(f"{a} + {b} = {result}")
        return result

    def subtract(self, a, b):
        result = a - b
        self.history.append(f"{a} - {b} = {result}")
        return result

    def multiply(self, a, b):
        result = a * b
        self.history.append(f"{a} * {b} = {result}")
        return result

    def divide(self, a, b):
        if b == 0:
            raise ValueError("Cannot divide by zero.")
        result = a / b
        self.history.append(f"{a} / {b} = {result}")
        return result

    def get_history(self):
        return self.history
    
    def clear_history(self):
        self.history.clear()
        return "History cleared."
    
def main():
    print("Welcome to the Calculator !")
    calc = Calculator()
    print("Choose an operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. View History")
    print("6. Clear History")
    print("7. Exit")

    while True:
        choice = input("Enter your choice (1-7): ")
        if choice == '1':
            a = float(input("Enter first number : "))
            b = float(input("Enter second number : "))
            print(f"Result: {calc.add(a,b)}")
        
        elif choice == '2':
            a = float(input("Enter first number : "))
            b = float(input("Enter second number : "))
            print(f"Result: {calc.subtract(a,b)}")

        elif choice == '3':
            a = float(input("Enter first number : "))
            b = float(input("Enter second number : "))
            print(f"Result: {calc.multiply(a,b)}")

        elif choice == '4':
            a = float(input("Enter first number : "))
            b = float(input("Enter second number : "))
            try:
                print(f"Result: {calc.divide(a,b)}")
            except ValueError as e:
                print(e)

        elif choice == '5':
            history = calc.get_history()
            if history:
                print("\nCalculation History:")
                for entry in history:
                    print(entry)
            else:
                print("No history available.")

        elif choice == '6':
            print(calc.clear_history())

        elif choice == '7':
            print("Exiting the calculator.!")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()