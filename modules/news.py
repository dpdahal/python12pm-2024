import datetime

# print(datetime.datetime.now())
# print(datetime.datetime.today())

# b_date = datetime.datetime(1993, 5, 10)
# today = datetime.datetime.today()
# print(today - b_date)


jobs =[
    {'title':"python developer",  "exp_date": "2023-10-10"},
    {'title':"java developer",  "exp_date": "2024-5-20"},
    {'title':"c# developer",  "exp_date": "2022-12-10"}
]

# exp_date ="2023-10-10"
for i in jobs:
    exp_date = datetime.datetime.strptime(i['exp_date'], "%Y-%m-%d")
    today= datetime.datetime.today()
    if exp_date>today:
        print ("job is still available")
    else:
        print ("the job is expired")