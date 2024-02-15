print("==============User Record==========")
print("1. Add User")
print("2. View User")
print("3. Search User")

option =int(input("Enter your option: "))
if option==1:
    handle = open("usersrecord\database.txt", "a")
    name = input("Enter your name: ")
    email = input("Enter your email: ")
    address = input("Enter your address: ")
    handle.write(f"{name} {email} {address}")
    handle.write("\n")
    handle.close()
    print("User added successfully")
elif option==2:
    print("Name\tEmail\tAddress")
    handle = open("usersrecord\database.txt", "r")
    for data in handle:
        print(data)
    handle.close()
elif option==3:
     search = input("Enter the name to search: ")
     handle = open("usersrecord\database.txt", "r")
     for data in handle:
            if search in data:
                print(data)

else:
    print("Invalid option")