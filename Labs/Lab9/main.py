try:
    x = int(input("Enter a number: "))
    result = 10 / x
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")
except ValueError:
    print("Error: Invalid input. Please enter a number.")

try:
    x = int(input("Enter a number: "))
    result = 10 / x
except (ValueError, TypeError, ZeroDivisionError):
    print("Please enter a number.")
else: print("Result:", int(result))

try:
    file = open("example.txt", "r")
    content = file.read()
except FileNotFoundError:
    print("File not found.")
finally:
    print("File closed.")
    file.close()

def withdraw(amount, balance):
    if amount > balance:
        print("Error: Insufficient balance.")
    return balance - amount
try:
    new_balance = withdraw(200, 100)
except ValueError as e:
    print(f"Error: {e}")

class Shape:
    def area(self):
        raise NotImplementedError("Subclasses must implement the 'area' method.")

class NegativeNumberError(Exception):
    def __init__(self, message="Negative numbers are not allowed."):
        self.message = message
        super().__init__(self.message)

def square_root(number):
    if number < 0:
        raise NegativeNumberError("Cannot compute square root of negative numbers.")
    return number ** 0.5

try:
    result = square_root(-9)
except NegativeNumberError as e:
    print(f"Error: {e}")

class ApplicationError(Exception):
    """Base class for all application-related errors."""
    pass

class DatabaseError(ApplicationError):
    """Raised for database-related errors."""
    pass

class ValidationError(ApplicationError):
    """Raised for input validation errors."""
    pass

try:
    raise ValidationError("Invalid input data.")
except ValidationError as e:
    print(f"Validation error: {e}")
except ApplicationError as e:
    print(f"Application error: {e}")

def add(a, b):
    print(f"a: {a}, b: {b}")
    return a + b
print(add(2, 3))

def divide(a, b):
    assert b != 0, "Division by zero is not allowed."
    return a / b
print(divide(10, 0))