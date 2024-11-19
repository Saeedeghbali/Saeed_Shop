from itertools import product
from pickle import GET
from token import NAME
from unicodedata import name
from flask import Flask, Request, redirect, render_template, request, session, abort,url_for
from flask.blueprints import Blueprint
import config
from models.product import Product
from extentions import db   
app=Blueprint("admin",__name__)

@app.before_request
def before_request():
    if session.get('admin_login', None) == None and request.endpoint != 'admin.login':
        abort(403)

@app.route('/admin/login',methods=["POST","GET"])
def login():
    if request.method == "POST":
        username= request.form.get ("username", None)
        password= request.form.get ("password", None)
        if username == config.ADMIN_USERNAME and password==config.ADMIN_PASSWORD:
            session['admin_login'] = username
            return redirect("/admin/dashboard")
        else:
            return redirect("/admin/login")  
    else:
        return render_template("admin/login.html")

@app.route('/admin/dashboard',methods=["GET","POST"])
def dashboard():
    return render_template('admin/dashboard.html')

@app.route('/admin/dashboard/products',methods=["GET","POST"])
def Products():
         
    if request.method=="GET":
        Products = Product.query.all()
        return render_template('admin/products.html',products = Products)
    else:
        name = request.form.get("name",None)
        price = request.form.get("price",None)
        discriptin  =request.form.get("discriptin",None)
        active  =request.form.get("active",None)
        p = Product(name=name,price=price,discriptin=discriptin)

        if active == None:
            p.active= 0
        else:
            p.active=1

        db.session.add(p)
        db.session.commit()
        return "انجام شد"
@app.route('/admin/dashboard/edit-product/<id>',methods=["GET","POST"])
def edit_Product(id):
    product = Product.query.filter(Product.id == id).first_or_404()     
    if request.method=="GET":
        
        return render_template('admin/edit-product.html',product = product)
    else:
        name = request.form.get("name",None)
        price = request.form.get("price",None)
        discriptin  =request.form.get("discriptin",None)
        active  =request.form.get("active",None)
        
        product.name=name
        product.price=price
        product.discriptin=discriptin
        if active == None:
            product.active= 0
        else:
            product.active=1

        db.session.commit()
        return redirect(url_for("admin.edit_Product", id=id))