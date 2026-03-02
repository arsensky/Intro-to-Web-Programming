name = input("Enter your name: ")
age = int(input("Enter your age: "))
print(f"Your name is {name} and your age is {age}.")

a, b, c = map(int, input("Enter three numbers separated by space: ").split())
sum = a + b + c
average = sum / 3
product = a * b * c
print(f"sum: {sum}, average: {average}, product: {product}")