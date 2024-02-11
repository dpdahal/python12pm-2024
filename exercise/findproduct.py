category=[
    {'cid':1,'cat_name':'mobile'},
    {'cid':2,'cat_name':'laptop'},
    {'cid':3,'cat_name':'tv'},
    {'cid':4,'cat_name':'watch'},
    {'cid':5,'cat_name':'headset'}
]

products=[
    {'pid':1,'name':'samsung','price':10000,'cid':1},
    {'pid':2,'name':'nokia','price':20000,'cid':1},
    {'pid':3,'name':'dell','price':30000,'cid':2},
    {'pid':4,'name':'hp','price':40000,'cid':2},
    {'pid':5,'name':'sony','price':50000,'cid':3}
]

def search(criteria=''):
    new_list = []
    for product in products:
        for cat in category:
            if product['cid'] == cat['cid']:
                new_list.append({**product, **cat})
    if criteria:
         for data in new_list:
            if data['cat_name'] == criteria or data['name']==criteria or str(data['cid'])==str(criteria):
                print(data)
    else:
        print(new_list)            

search()