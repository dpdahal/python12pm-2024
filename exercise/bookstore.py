users=[
    {"username":"admin","password":"admin"},
    {"username":"sophia","password":"sophia"},
    {"username":"john","password":"john"}
]
books=[
    {"title":"The Alchemist","author":"Paulo Coelho","price":10},
    {"title":"The Monk who sold his Ferrari","author":"Robin Sharma","price":15},
    {"title":"The Power of Now","author":"Eckhart Tolle","price":20},
    {"title":"The Secret","author":"Rhonda Byrne","price":25}
]
username=input("Enter username: ")
password = input("Enter password: ")
is_login=False
for user in users:
    if user["username"]==username and user["password"]==password:
        is_login=True
        print("title, author, price")
        for book in books:
            print(f"{book['title']}, {book['author']}, {book['price']}")
       
if not is_login:
    print("Invalid username or password")
