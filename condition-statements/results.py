print("=============ABC==============")
num = int(input("number of students: "))
increment=1
students_marks=[]

while increment<=num:
    print(f"=========Student:{increment}============= ")
    for a in range(1):
        nep = int(input("Enter nep mark: "))
        eng = int(input("Enter eng mark: "))
        mat = int(input("Enter mat mark: "))
        sic = int(input("Enter sic mark: "))
        pop = int(input("Enter pop mark: "))
        total = nep+eng+mat+sic+pop
        students_marks.append(total)

    increment+=1



print("=============RESULT==============")
s_id=1
for mark in students_marks:
    per = mark/5
    grade =""
    if per>35 and per<=45:
        grade="D"
    elif per>45 and per<=60:
        grade="C"
    elif per>60 and per<=80:
        grade="B"
    elif per>80:
        grade="A"
    else:
        print("Grade: D")
    print(f"Student {s_id} got {mark} marks and {per} percentage and grade {grade}")
    s_id+=1
    