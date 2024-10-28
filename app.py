"""
This script runs the application using a development server.
It contains the definition of routes and views for the application.
"""

from flask import Flask
from blueprints.general import app as general
from blueprints.user import app as user
from blueprints.admin import app as admin

app = Flask(__name__)

# Make the WSGI interface available at the top level so wfastcgi can get it.
wsgi_app = app.wsgi_app

app.register_blueprint(general)
app.register_blueprint(user)
app.register_blueprint(admin)

@app.route('/')
def hello():
    """Renders a sample page."""
    return "Hello World!"

if __name__ == '__main__':
    import os
    HOST = os.environ.get('SERVER_HOST', 'localhost')
    try:
        PORT = int(os.environ.get('SERVER_PORT', '5555'))
    except ValueError:
        PORT = 5555
    app.run(HOST, PORT)
