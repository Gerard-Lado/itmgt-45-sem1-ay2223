from flask import Flask, redirect
from flask import render_template
from flask import request
from flask import session
from bson.json_util import loads, dumps
from flask import make_response
import logging

import database as db
import ordermanagement as om
import authentication


app = Flask(__name__)

#super secret key, shhhh
app.secret_key = b'sh@b@l@b@d1ngd0ng'

logging.basicConfig(level=logging.DEBUG)
app.logger.setLevel(logging.INFO)

@app.route('/login', methods=['GET', 'POST'])
def login():
    return render_template('login.html')

@app.route('/auth', methods = ['GET', 'POST'])
def auth():
    username = request.form.get('username')
    password = request.form.get('password')

    is_successful, user = authentication.login(username, password)
    app.logger.info('%s', is_successful)
    session["error"] = 1
    if(is_successful):
        session["user"] = user
        print(session["user"])
        session.pop("error", None)
        return redirect('/')
    else:
        return redirect('/login')

@app.route('/changepasswordscreen', methods=['GET', 'POST'])
def changepasswordscreen():
    return render_template('changepassword.html')

@app.route('/changepassword', methods = ['GET', 'POST'])
def changepassword():
    user = session["user"]["username"]
    current_password = request.form.get('currentpassword')
    new_password = request.form.get('newpassword')
    confirmation = request.form.get('confirmation')
    session["error"] = 1
    if current_password == session["user"]["password"]:
        if new_password == confirmation:
            db.change_password(user, new_password)
            session.pop("error", None)
            return redirect('/')
        else:
            return redirect('/changepasswordscreen')
    else:
        return redirect('/changepasswordscreen')



@app.route('/')
def index():
    return render_template('index.html', page="Index")

@app.route('/products')
def products():
    product_list = db.get_products()
    return render_template('products.html', page="Products", product_list=product_list)

@app.route('/branches')
def branches():
    branch_list = db.get_branches()
    return render_template('branches.html', page="Branches", branch_list=branch_list)

@app.route('/addtocart', methods = ['GET', 'POST'])
def addtocart():
    quantity = int(request.form.get('qty'))
    code = request.form.get('code')
    product = db.get_product(int(code))
    item=dict()

    item["qty"] = quantity
    item["name"] = product["name"]
    item["subtotal"] = product["price"]*item["qty"]

    if(session.get("cart") is None):
        session["cart"]={}

    cart = session["cart"]
    cart[code]=item
    session["cart"]=cart
    return redirect('/cart')

@app.route('/removefromcart', methods = ['GET', 'POST'])
def removefromcart():
    name = request.form.get('name')
    print(name)
    subtotal = float(request.form.get('subtotal'))
    print(subtotal)
    qty = float(request.form.get('qty'))
    print(qty)
    code = str(db.code_from_value(name))

    cart = session["cart"]
    cart.pop(code)
    session["cart"]=cart
    return redirect('/cart')

@app.route('/checkout')
def checkout():
    # clear cart in session memory upon checkout
    om.create_order_from_cart()
    session.pop("cart",None)
    return redirect('/ordercomplete')

@app.route('/ordercomplete')
def ordercomplete():
    return render_template('ordercomplete.html')


@app.route('/cart')
def cart():
    return render_template('cart.html')

@app.route('/productdetails')
def productdetails():
    code = request.args.get('code', '')
    product = db.get_product(int(code))

    return render_template('productdetails.html', code=code, product=product)

@app.route('/aboutus')
def aboutus():
    return render_template('aboutus.html', page="About Us")

@app.route('/pastorders')
def pastorders():
    user = session["user"]["username"]
    order_list = db.get_orders(user)
    return render_template('pastorders.html', page="Paso Orders", order_list=order_list)

@app.route('/logout')
def logout():
    session.pop("user",None)
    session.pop("cart",None)
    return redirect('/')

@app.route('/api/products', methods=['GET'])
def api_get_products():
    resp = make_response(dumps(db.get_products()))
    resp.mimetype='application/json'
    return resp

