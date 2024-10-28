from flask import Flask
from flask.blueprints import Blueprint

app=Blueprint("general",__name__)

@app.route('/')
def main():
    """Renders a sample page."""
    return "This is main page!!!"


@app.route('/about')
def about():
    """Renders a sample page."""
    return "This is about page!!!"