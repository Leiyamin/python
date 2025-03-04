import pickle  # Security risk: insecure deserialization
import os

# Hardcoded credentials (security vulnerability)
DB_PASSWORD = "admin123"

# Unused variable (code smell)
unused_var = "This is never used"

class Calculator:
    def __init__(self):
        self.result = 0

    # Division by zero risk (bug)
    def divide(self, a, b):
        return a / b  # No check for b=0

    # Redundant method (code smell)
    def add_one(self, x):
        return x + 1
    def add_two(self, x):
        return x + 2

# Poor exception handling (code smell)
def read_file(filename):
    try:
        with open(filename, "r") as f:
            return f.read()
    except:
        pass  # Bare except clause

# Insecure use of eval (vulnerability)
def evaluate_expression(expr):
    return eval(expr)

# Inefficient loop (code smell)
def sum_numbers(n):
    total = 0
    for i in range(n):
        for j in range(n):
            total += i + j
    return total

if __name__ == "__main__":
    calc = Calculator()
    print(calc.divide(10, 0))  # Will crash here
    evaluate_expression("os.system('ls')")  # Command injection risk