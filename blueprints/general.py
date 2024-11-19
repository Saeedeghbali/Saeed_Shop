
from flask import Flask,render_template
from flask.blueprints import Blueprint

from models.product import Product as pd

app=Blueprint("general",__name__)

@app.route('/')
def main():
    #products = Product.query.filter(Product.active == 1).all()
    products=pd.query.filter(pd.active == 1).all()
    """Renders a sample page."""
    return render_template("main.html", products = products)

@app.route("/product/<int:id>/<name>")
def Product(id,name):
    
    product=pd.query.filter(pd.id == id).filter(pd.name == name).filter(pd.active == 1).first_or_404()
    
    return render_template('product.html',product=product)

@app.route('/about')
def about():
    """Renders a sample page."""
    return render_template("about.html")