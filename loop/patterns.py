print("=========Emp Record============")
num =int(input("Enter the number of employees: "))
emp_details = []
salary_range = [10000,20000,30000,40000,50000]
role_range = [1,2]
x=1
while x<=num:
    for a in range(1):
        name = input("Enter the name: ")
        salary = int(input("Enter the salary: "))
        if not salary in salary_range:
            print("Invalid Salary")
            exit()       
        else:
            print("Role: 1. Frontend 2. Backend")
            role =int(input("Enter the role: "))
            if not role in role_range:
                print("Invalid Role")
                exit()
          
            data={
                "name":name,
                "salary":salary,
                "role":role
            }
            emp_details.append(data)

    x+=1

print("=========Emp Details============")
print("Sn,Name, Salary, Role")
x=1
for emp in emp_details:
    print(f"{x},{emp['name']},{emp['salary']},{emp['role']}")
    x+=1
    