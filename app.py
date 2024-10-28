from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from blueprints.general import app as general
from blueprints.user import app as user
from blueprints.admin import app as admin

app = Flask(__name__)
wsgi_app = app.wsgi_app

app.register_blueprint(general)
app.register_blueprint(user)
app.register_blueprint(admin)

db=SQLAlchemy()

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"

db.init_app(app)

with app.app_context():
    db.create_all()

if __name__ == '__main__':
    import os
    HOST = os.environ.get('SERVER_HOST', 'localhost')
    try:
        PORT = int(os.environ.get('SERVER_PORT', '5555'))
    except ValueError:
        PORT = 5555
    app.run(HOST, PORT)
