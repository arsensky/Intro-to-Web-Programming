import json

# Converting a Dictionary to JSON
data = {
    "name": "Alice",
    "age": 25,
    "city": "New York"
}

json_string = json.dumps(data)
print(json_string)

# Writing JSON to a File
with open("data.json", "w") as file:
    json.dump(data, file)

# Reading JSON from a File
with open("data.json", "r") as file:
    loaded_data = json.load(file)
print(loaded_data)

# Converting JSON String to Dictionary
json_string = '{"name": "Alice", "age": 25, "city": "New York"}'
data = json.loads(json_string)
print(data["name"])
print(type(data))

# Converting a List to JSON
users = [
    {"name": "Alice", "age": 25},
    {"name": "Bob", "age": 30},
    {"name": "Charlie", "age": 22}
]
json_string_users = json.dumps(users, indent=4) # pretty-printing json
print(json_string_users)

# Handling Invalid JSON
invalid_json = '{"name": "Alice", "age": 25, "city": "New York"}'
try:
    data = json.loads(invalid_json)
except json.JSONDecodeError as e:
    print(f"Error loading JSON: {e}")

# Example 1: Converting Python Data to JSON (Serialization)
student_data = {
    "name": "Alice",
    "age": 21,
    "courses": ["Math", "Science", "History"]
}
json_string = json.dumps(student_data, indent=4)
print("Serialized json string:")
print(json_string)

# Example 2: Converting JSON Back to Python Data (Deserialization)
json_string = '''
{
    "name": "Alice",
    "age": 21,
    "courses": ["Math", "Science", "History"]
}
'''
student_data = json.loads(json_string)
print("Deserialized json string:")
print(student_data)

# Example 3: Reading from and Writing to a JSON File
student_data = {
    "name": "Alice",
    "age": 21,
    "courses": ["Math", "Science", "History"]
}

with open("student.json", "w") as file:
    json.dump(student_data, file, indent=4)

print("Data has been written to student.json")

## Reading JSON from a File
with open("student.json", "r") as file:
    data_loaded = json.load(file)

print("Data loaded from student.json:")
print(data_loaded)

# Exercise 1: Converting a Python Dictionary to a JSON String (Serialization)
student_data = {
    "name": "Aitegin",
    "age": 15,
    "city": "Karakol",
    "courses": ["Math", "Science", "History"]
}
json_string = json.dumps(student_data, indent=4)
print("Serialized json string:")
print(json_string)

# Exercise 2: Converting a JSON String Back to a Python Object (Deserialization)
json_string = '''{"name": "Aitegin", "age": 15, "city": "Karakol", "courses": ["Math", "Science", "History"]}'''
student_data = json.loads(json_string)
print("Deserialized json string:")
print(student_data)

# Exercise 3: Reading from and Writing to a JSON File
student_data = {
    "name": "Aitegin",
    "age": 15,
    "city": "Karakol",
    "courses": ["Math", "Science", "History"]
}

filename = "student2.json"
with open(filename, "w") as file:
    json.dump(student_data, file, indent=4)
print(f"Data has been written to {filename}")

with open(filename, "r") as file:
    data_loaded = json.load(file)

print("Data loaded from student.json:")
print(data_loaded)