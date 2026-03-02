# Example 1: Basic Text File Operations
filename = 'example.txt'
content_to_write = "Hello, world!\nWelcome to file handling in Python."

with open(filename, 'w') as file:
    file.write(content_to_write)

print(f"Content written to {filename}.")

with open(filename, 'r') as file:
    content_read = file.read()

print("Content read from file:")
print(content_read)

# Example 2: Processing CSV Files
import csv

data = [
    ["Name", "Age", "City"],
    ["Alice", 30, "New York"],
    ["Bob", 25, "Los Angeles"],
    ["Charlie", 35, "Chicago"]
]

csv_filename = 'people.csv'
with open(csv_filename, 'w', newline="") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(data)

print(f"Data written to {csv_filename}.")

with open(csv_filename, 'r') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        print(row)

# Example 3: Appending Data to a File
filename = 'example.txt'
additional_content = "\nAppending new lines to the file."

with open(filename, 'a') as file:
    file.write(additional_content)

print(f"New content appended to {filename}.")

with open(filename, 'r') as file:
    content_read = file.read()

print("Updated content to file:")
print(content_read)

### Lab Exercises
# ex. 1
filename = 'sample_text.txt'
content = """Hello, world!
This is a simple text file.
It contains multiple lines of text testing file operations."""

with open(filename, 'w') as file:
    file.write(content)
print(f"Content has been written to {filename}.")

with open(filename, 'r') as file:
    read_content = file.read()

print("Content read from file:")
print(read_content)

# ex. 2
csv_filename2 = 'people2.csv'
data = [
    ["Name", "Age", "City"],
    ["Alice", 30, "New York"],
    ["Bob", 25, "Los Angeles"],
    ["Charlie", 35, "Chicago"]
]

with open(csv_filename2, 'w', newline="") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(data)
print(f"Data written to {csv_filename2}.")

with open(csv_filename2, 'r', newline="") as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        print(row)

# ex. 3
filename = 'sample_text2.txt'
additional_text = "\nThis line is appended to the file."

with open(filename, 'a') as file:
    file.write(additional_text)
print(f"New content appended to {filename}.")

with open(filename, 'r') as file:
    content_read = file.read()

print("Content read from file:")
print(content_read)