# What is file handling?
# File handling is an store and retrieve data from a file.
# open()
# file name
# mode: r, w, a, r+
# r- read
# w- write
# a- append
# r+- read and write

# types of files: text and binary

# handle = open("filehandling/users.txt", "w")
# handle = open("filehandling/users.txt", "a")
# handle.write("laxmi")
# handle.write("\n")
# handle.write("ram")
# handle.write("\n")
# handle.close()
# name,email,address,phone
# ram,ram@gmail.com,kathmandu,9876543210
# shyam,shyam@gmail.com,lalitpur,9876543210

fdata = open("filehandling/users.txt", "r")
# print(fdata.read())
# print(fdata.readline())
print(fdata.readlines())