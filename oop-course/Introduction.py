# What is oop?
# OOP is a programming paradigm that uses "objects" to design applications and 
# computer programs.
# What is an object?
# An object is a collection of data and methods that operate on the data.
# What is a class?
# A class is a blueprint for creating objects.
# What is a method?
# A method is a function that is associated with a class.
# What is property?
# A property is a class variable or instance variable that holds data.
# What is self?
# self is a reference to the current instance of the class.

# class Students:
#     x=10
#     y=20

#     def test(self,a):
#         # obj = Students()
#         print(self.x,a)

# obj= Students()
# obj.text()


class Calculator:

    def add(self,x,y):
        print(x+y)

    def sub(self,x,y):
        print(x-y)

x = int(input("Enter the first number: "))
y = int(input("Enter the second number: "))
obj = Calculator()
obj.add(x,y)
obj.sub(x,y)


    
