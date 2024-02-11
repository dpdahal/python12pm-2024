category=[
    {'cid':1,'name':'mobile'},
    {'cid':2,'name':'laptop'},
    {'cid':3,'name':'tv'},
    {'cid':4,'name':'watch'},
    {'cid':5,'name':'headset'}
]

products=[
    {'pid':1,'name':'samsung','price':10000,'cid':1},
    {'pid':2,'name':'nokia','price':20000,'cid':1},
    {'pid':3,'name':'dell','price':30000,'cid':2},
    {'pid':4,'name':'hp','price':40000,'cid':2},
    {'pid':5,'name':'sony','price':50000,'cid':3}
]

search = input("Enter the category name: ")
not_found = True
for pc in category:
    if pc['name']==search:
        print("pid,name,price,cid,category_name")
        for product in products:
            if product['cid']==pc['cid']:
                print(f"{product['pid']},{product['name']},{product['price']},{product['cid']},{pc['name']}")
                not_found = False       

if not_found:
    print("Category not found")