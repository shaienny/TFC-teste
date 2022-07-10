from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:root@localhost/flask_login'
app.config['SECRET_KEY'] = 'root'

login_manager = LoginManager(app)
db = SQLAlchemy(app)


