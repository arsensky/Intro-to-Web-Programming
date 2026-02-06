# 1. Calculating the square
def square(number):
    return number ** 2
print("Square is", square(20))

# 2. Returning the sum
def sum_list(numbers):
    return sum(numbers)
print("\nSum of all numbers:", sum_list([1, 2, 3, 4, 5]))

# 3. Fibonacci sequence
def fibonacci(number):
    if number <= 1:
        return number
    return fibonacci(number - 1) + fibonacci(number - 2)
print("\nFibonacci is", fibonacci(10))

# 4. Prime number
def prime_number(number):
    if number <= 1:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True
a, b = 5, 10
print(f"\n{a} is prime: {prime_number(a)}")
print(f"{b} is prime: {prime_number(b)}")