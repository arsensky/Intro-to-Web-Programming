# Example 1
class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def display_info(self):
        return f"{self.brand} {self.model} {self.year}"

car1 = Car("Toyota", "Raum", 2004)
car2 = Car("Honda", "Civic", 2019)

print(car1.display_info())
print(car2.display_info())

# Example 2
class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

    def bark(self):
        return f"{self.name} says Woof!"

dog1 = Dog("Buddy", "Golden Retriever")
print(dog1.bark())

# Example 4
class Employee:
    company = "TechCorp"

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

e1 = Employee("Alice", 50000)
e2 = Employee("Bob", 60000)

print(e1.company)
print(e2.company)

Employee.company = "NewTechCorp"

print(e1.company)
print(e2.company)

# USER AUTHENTIFICATION SYSTEM Example
class User:
    def __init__(self, username, password):
        self.username = username
        self.__password = password

    def login(self, password):
        if password == self.__password:
            return f"Welcome, {self.username}!"
        else: return "Invalid credentials!"

user = User("admin", "secure123")

print(user.login("secure123"))
print(user.login("admin"))

# Encapsulation Using
class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.__balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited {amount}. New balance: {self.__balance}.")

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print(f"Withdrawn {amount}. Remaining balance: {self.__balance}.")
        else: print("Insufficient funds!")

    def get_balance(self):
        return self.__balance

account = BankAccount("Alice", 1000)
account.deposit(500)
account.withdraw(300)
print(account.get_balance())

# Inheritance Using
## Parent class
class Animal:
    def __init__(self, name):
        self.name = name

    def make_sound(self):
        return "Some sound"

## Child classes
class Dog(Animal):
    def make_sound(self):
        return "Woof!"

class Cat(Animal):
    def make_sound(self):
        return "Meow!"

dog = Dog("Buddy")
cat = Cat("Whiskers")

print(dog.name, "says:", dog.make_sound())
print(cat.name, "says:", cat.make_sound())

# Polymorphism Using
class Bird:
    def fly(self):
        return "Flying high!"

class Airplane:
    def fly(self):
        return "Taking off into the sky!"

class Fish:
    def fly(self):
        return "I can't fly!"

for obj in [Bird(), Airplane(), Fish()]:
    print(obj.fly())

# Abstraction Using
from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def start_engine(self):
        pass

class Car(Vehicle):
    def start_engine(self):
        print("Car engine started!")

class Bike(Vehicle):
    def start_engine(self):
        print("Bike engine started!")

car = Car()
bike = Bike()

car.start_engine()
bike.start_engine()

# OOP in a Library Management System Example
class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    def display_info(self):
        return f"{self.title} by {self.author} ({self.year})"

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def list_books(self):
        for book in self.books:
            print(book.display_info())

book1 = Book("1984", "George Orwell", 1949)
book2 = Book("To Kill a Mockingbird", "Harper Lee", 1960)
library = Library()
library.add_book(book1)
library.add_book(book2)
library.list_books()