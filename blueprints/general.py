from itertools import product
from flask import Flask,render_template
from flask.blueprints import Blueprint
from models.product import Product
app=Blueprint("general",__name__)

@app.route('/main')
def main():
    products = Product.query.all()
    """Renders a sample page."""
    return render_template("main.html",products=products)


@app.route('/about')
def about():
    """Renders a sample page."""
    return render_template("about.html")