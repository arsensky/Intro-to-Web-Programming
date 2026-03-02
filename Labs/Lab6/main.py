# 1. Different types input and output
INTEGER = int(input("Enter an integer: "))
FLOAT = float(input("Enter a float: "))
STRING = str(input("Enter a string: "))
print(f"types: first is {type(INTEGER)}, second is {type(FLOAT)}, third is {type(STRING)}.")

# 2. Converting types and Creating a Dictionary
text = "2026"
number = int(text)
float_number = float(number)

person = {
    "name" : "Arsen",
    "age" : 20,
    "weight" : 70,
    "height" : 185,
}
print(f"{person['name']} is {person['age']} years old with weight {person['weight']} kg and height {person['height']} centimeters.")

# 3. Creating a Set
new_set = {10, 20, 30, 40, 50, 60, 70, 80, 90, 90}
new_set.add(100)
new_set.remove(90)
print (50 in new_set)