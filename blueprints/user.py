from flask import Flask
from flask.blueprints import Blueprint

app=Blueprint("userl",__name__)

@app.route('/user')
def user():
    """Renders a sample page."""
    return "This is user page!!"
