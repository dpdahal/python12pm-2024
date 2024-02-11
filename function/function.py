# What is function?
# Function is a resuable block of code that does a specific task.  when it was run it was cas

# types of function
# 1. Built-in function: print(), input(), len(), range(), etc
# 2. User-defined function: we can create our own function

# def hello():
#     print("Hello World")

# hello()
# hello()

# function with parameter

# def hello(name):
#     print("Hello", name)

# hello('ram')
# hello('shyam')

# def add(x,y):
#     print(x+y)

# add(10,20)
# add(30,40)

#  default or optional parameter

# def user(name,phone,age=0):
#     print("Name:", name)
#     print("Age:", age)

# # user('ram')
# user('shyam',9876)

# function accept any number of argument

# def users(data):
#     print(data)

# users(['ram','sita','gita','hari'])

# *args
# **kwargs


# def users(*data,**info):
#     print(data)
#     print(info)

# users('ram','sita','gita','hari',name='hari',age=50)

# print()


# function return value

# def add(x,y):
#     return x+y
#     return 6+8

# print(add(7,9))
# a = add(7,9)
# print(a)
# a = add
# print(a(7,9))


# def add_sub(x,y):
#     t = x+y
#     s = x-y
#     return [t,s]

# a = add_sub(10,5)
# print(a)



# function scope
# 1. Local scope
# 2. Global scope


# x=5

# def test():
#     global x
#     x =x+7
#     print(x)
  

# test()
# print(x)

# def take_value():
#     return [67,89]

# def display():
#     print(take_value())

# display()




# def my_pepeat(time,data):
#     for i in range(time):
#         print(data)


# my_pepeat(5,'Hello World')


# data=[
#     {'name':'ram','gender':"male"},
#     {'name':'hari','gender':"male"},
#     {'name':'sita','gender':"female"},
#     {'name':"laxmi","gender":"female"}
# ]
# def search(criteria):
#     for u in data:
#         if u['name']==criteria or u['gender']==criteria:
#             print(u)
# criteria = input("Enter any criteria: ")
# search(criteria)

# def male(data):
#     for u in data:
#         if u['gender']=='male':
#             print(u['name'])

# def female(data):
#      for u in data:
#         if u['gender']=='male':
#             print(u['name'])

# male(data)
# female(data)