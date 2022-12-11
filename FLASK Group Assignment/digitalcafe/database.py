import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")

products_db = myclient["products"]
order_management_db = myclient["order_management"]

#joben@example.com
#Ch@ng3m3!

def code_from_value(name):
    products_coll = products_db["products"]
    product = products_coll.find_one({"name":name})
    code = product["code"]
    return code

def get_products():
    product_list = []

    products_coll = products_db["products"]

    for p in products_coll.find({}, {"_id":0}):
        product_list.append(p)

    return product_list

def get_product(code):
    products_coll = products_db["products"]

    product = products_coll.find_one({"code":code}, {"_id":0})

    return product

def get_branches():
    branch_list = []

    branches_coll = products_db["branches"]

    for p in branches_coll.find({}):
        branch_list.append(p)

    return branch_list

def get_branch(code):
    branches_coll = products_db["branches"]

    branch = branches_coll.find_one({"code":code})

    return branch

def get_user(username):
    customers_coll = order_management_db['customers']
    user = customers_coll.find_one({"username":username})
    return user

def change_password(user, new_password):
    customers_coll = order_management_db['customers']
    customers_coll.update_one({'username':user}, {"$set":{"password":new_password}})

def create_order(order):
    orders_coll=order_management_db['orders']
    orders_coll.insert(order)

def get_orders(user):
    transaction_list = []
    order_list = []
    orders_coll = order_management_db["orders"]

    for p in orders_coll.find({"username":user}):
        transaction_list.append(p)
    for q in transaction_list:
        for r in range(len(q.get('details'))):
            order_list.append(q.get('details')[r])
    print(transaction_list)
    return order_list
