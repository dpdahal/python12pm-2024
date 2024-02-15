# what is exception handling?
# Exception handling is a way to handle errors 
# that might occur in your code.

# print("exception handling")

# print(10/0)

# print("Hello ")

# try:
#     print(10/0)
# except Exception as e:
#     print("Error: ", e)

# print("Hello ")

# try:
#     print(10/0)
# except ZeroDivisionError as e:
#     print("Error: ", e)
# finally:
#     print("This will always be executed")


def add(x,y):
    if y==0:
        raise Exception("y cannot be zero")
    return x/y

try:
    print(add(10,9))
except Exception as e:
    print("Error: ", e)

# ZeroDivisionError
# ValueError
# TypeError
# FileNotFoundError
# ImportError