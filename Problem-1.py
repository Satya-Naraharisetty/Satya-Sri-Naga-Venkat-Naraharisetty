class Calculator:
    def __init__(self, a: float, b: float, operation: str):
        self.a = a
        self.b = b
        self.operation = operation.lower()

    def calculate(self):
        if self.operation == "add":
            return self.a + self.b
        elif self.operation == "subtract":
            return self.a - self.b
        elif self.operation == "multiply":
            return self.a * self.b
        elif self.operation == "divide":
            if self.b == 0:
                raise ValueError("Division by zero is not allowed.")
            return self.a / self.b
        else:
            raise ValueError("Invalid operation type.")

if __name__ == "__main__":
    try:
        a = float(input("Enter value for a: "))
        b = float(input("Enter value for b: "))
        operation = input("Enter operation (add, subtract, multiply, divide): ")
        calc = Calculator(a, b, operation)
        result = calc.calculate()
        print("Result:", result)
    except Exception as e:
        print("Error:", e)