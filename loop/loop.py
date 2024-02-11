# data=[
#     {'name':"ram", 'address':"ktm"},
#     {'name':"shyam", 'address':"bkt"},
#     {'name':"hari", 'address':"lalitpur"},
# ]

# for user in data:
#     print(user['name'])

# print(data[0]['name'])

# users=[
#     {'name':"ram", 'gender':"male",'status':True},
#     {'name':"sita", 'gender':"female",'status':False},
#     {'name':"hari", 'gender':"male",'status':False},
#     {'name':"laxmi", 'gender':"female",'status':True},
# ]

# name =input("Enter name: ")
# not_found=True
# for user in users:
#     if user['name']==name:
#         print(user)
#         not_found=False
        
# if not_found:
#     print("user not found")


# total_user=len(users)
# total_male=0
# total_female=0
# total_active=0
# total_inactive=0

# for user in users:
#     if user['gender']=='male':
#         total_male+=1
#     else:
#         total_female+=1

#     if user['status']==True:
#         total_active+=1
#     else:
#         total_inactive+=1

# print(f"Total user: {total_user}")
# print(f"Total male user: {total_male}")
# print(f"Total female user: {total_female}")
# print(f"Total active user: {total_active}")
# print(f"Total inactive user: {total_inactive}")



# data=[
#     [12,34,56,78],
#     [87,99,67,87]
# ]

# result =[99]

# a =0

# while a<10:
#     a+=1
#     if a==5:
#         continue
#     print(a)
   
lang ='english'

match lang:
    case 'nepali':
        print("Hello Nepali")
    case 'english':
        print("Hello English")
    case 'hindi':
        print("Hello Hindi")
    case _:
        print("Language not match")
