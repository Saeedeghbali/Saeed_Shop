from tkinter import ON
from flask import Flask
from flask_wtf.csrf import CSRFProtect
from blueprints.general import app as general
from blueprints.user import app as user
from blueprints.admin import app as admin
import config
import extentions
app = Flask(__name__)
wsgi_app = app.wsgi_app

app.register_blueprint(general)
app.register_blueprint(user)
app.register_blueprint(admin)



app.config["SQLALCHEMY_DATABASE_URI"] = config.SQLALCHEMY_DATABASE_URI
app.config["SECRET_KEY"]= config.SECRET_KEY
extentions.db.init_app(app)

csrf= CSRFProtect(app)

with app.app_context():
    extentions.db.create_all()

if __name__ == '__main__':
    import os
    HOST = os.environ.get('SERVER_HOST', 'localhost')
    try:
        PORT = int(os.environ.get('SERVER_PORT', '5555'))
    except ValueError:
        PORT = 5555
    app.run(HOST, PORT,debug=ON)
