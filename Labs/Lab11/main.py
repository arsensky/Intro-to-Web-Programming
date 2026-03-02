# 1. Basic List Operations
my_list = [10, 20, 30, 40, 50]
my_list.append(60)
my_list.insert(1, 15)
my_list.remove(30)
my_list.reverse()
my_list.sort()
print(my_list)

# 2. List Slicing and Indexing
print(my_list[:3])
print(my_list[-2:])
print(my_list[::-1])

# 3. Basic Dictionary Operations
my_dictionary = {"name": "Alice", "age": 22, "grade": "A"}
my_dictionary["subject"] = "Math"
my_dictionary["grade"] = "A+"
my_dictionary.pop("age")
print(my_dictionary.keys())
print(my_dictionary.values())
print(my_dictionary.items())

# 4. Set Operations
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}
union_set = set1.union(set2)
intersection_set = set1.intersection(set2)
difference_set = set1.difference(set2)
print(union_set)
print(intersection_set)
print(difference_set)

# 5. Tuple Methods
my_tuple = ("red", "blue", "green", "red", "yellow")
print(my_tuple.index("green"))
print(my_tuple.count("red"))

# 6. Working with Nested Lists and Dictionaries
company = {"employees": [
            {"name": "Bob", "position": "CEO", "salary": 50000},
            {"name": "Dylan", "position": "Manager", "salary": 40000},
            {"name": "Nicolas", "position": "Office Worker", "salary": 20000}]}
company["employees"].append({"name": "Jackson", "position": "Office Worker", "salary": 15000})
for employee in company["employees"]:
    print(employee["name"])