from flask import Flask
from flask.blueprints import Blueprint

app=Blueprint("general",__name__)

@app.route('/general')
def hello():
    """Renders a sample page."""
    return "This is Ggeneral page!!!"
