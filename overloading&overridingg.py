# overloading

# class human:
#     def sayHello(self,name=None):
#         if name is not None:
#             print('Hello'+ name)
#         else:
#             print('Hello')
# obj=human()
# obj.sayHello()
# obj.sayHello('vivanya')

# overriding

# class parent:
#     def myMethod(self):
#         print('Calling parent method')
# class child(parent):
#     def myMethod(self):
#         print('Callimg child method')
# c=child()
# c.myMethod()

# example 2

# class rectangle(object):
#     def __init__(self,length,width):
#         self.length=length
#         self.width=width
#     def area(self):
#         print('iii')
#         return self.length*self.width
#     def perimeter(self):
#         return 2*self.length+2*self.width
# class square(rectangle):
#     def __init__(self, length):
#         super().__init__(length, length)
# s = square(1)
# print(s.area())


#  Access Modifiers

# public

# class Student:
#    def __init__(self, name, age):
#       self.name = name
#       self.age = age
#    def display(self):
#       print("Name:", self.name)
#       print("Age:", self.age)
# s = Student("John", 20)
# s.display() 

# protected

# class Person:
#    def __init__(self, name, age):
#       self._name = name
#       self._age = age
    
#    def _display(self):
#       print("Name:", self._name)
#       print("Age:", self._age)

# class Student(Person):
#    def __init__(self, name, age, roll_number):
#       super().__init__(name, age)
#       self._roll_number = roll_number
    
#    def display(self):
#       self._display()
#       print("Roll Number:", self._roll_number)

# s = Student("John", 20, 123)
# s.display() 


# private

# class BankAccount:
#    def __init__(self, account_number, balance):
#       self.__account_number = account_number
#       self.__balance = balance
    
#    def __display_balance(self):
#       print("Balance:", self.__balance)

# b = BankAccount(1234567890, 5000)
# b.__display_balance() 


