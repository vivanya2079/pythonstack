# 1. Define a class which has at least two methods one, to get a string from console  input and other is to print the string in uppercase.

# class IOString():
#     def __init__(self):
#         self.str1 = ""

#     def get_String(self):
#         self.str1 = input()

#     def print_String(self):
#         print(self.str1.upper())

# print("Type in a statement and this program will make it upper case!")

# str1 = IOString()
# str1.get_String()
# str1.print_String()


# 2. Define a class, which have a class parameter and have a same instance parameter.

# class Student:
#     school = "freeCodeCamp.org"
    
#     def __init__(self, name, course):
#         self.name = name
#         self.course = course
    
# Student1 = Student("Jane", "JavaScript")
# Student2 = Student("John", "Python")

# print(Student1.name) 
# print(Student2.name) 



# 3. Define a class named Circle which can be constructed by radius. The Circle class has a method which can compute the area.

# class Circle():
#     def __init__(self, r):
#         self.radius = r

#     def area(self):
#         return self.radius**2*3.14
    
#     def perimeter(self):
#         return 2*self.radius*3.14

# NewCircle = Circle(8)
# print(NewCircle.area())
# print(NewCircle.perimeter())



# 4. Define a class named BankAccount. This class should contain methods withdraw() and deposit to calculate the balance amount remained in your account.

# class BankAccount():
#     def __init__(self,balance=0):
#         self.balance=balance
#     def deposit(self,amount):
#         if amount>0:
#             self.balance+=amount
#             return f"deposited ${amount}.Current balance:${self.balance}"
#         return "invalid deposit amount.amount must be greater than zero."
#     def withdraw(self,amount):
#         if amount >0 and amount <= self.balance:
#             self.balance -= amount
#             return f"withdraw ${amount}. current balance:$(self.balance)"
#         return "insufficint funds."if amount>0 else "invalid withdrawal amount."
#     def get_balance(self):
#         return f"current balance: ${self.balance}"
# account=BankAccount(1000)
# print(account.deposit(500))
# print(account.withdraw(200))
# print(account.get_balance())



# 5.Define a class named Shape and its subclass Square. The Square class has an init function which takes a length as argument. Both classes have a area function which can print the area of the shape where Shape's area is 0 by default. 

# class shape:
#     def __init__(self):
#         self.area=0
#     def calculate_area(self):
#         pass
# class square(shape):
#     def __init__(self,length):
#         super(). __init__()
#         self.length = length
    
#     def calculate_area(self):
#         self.area = self.length**2

# square1= square(5)
# square2= square(7)

# square1.calculate_area
# square2.calculate_area

# print(f"area of square 1:{square1.area}")
# print(f"area of square 2:{square2.area}")

# shape=shape()
# print(f"area of a generic shape:{shape.area}")