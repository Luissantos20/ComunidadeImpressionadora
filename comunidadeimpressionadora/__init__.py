from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
import os

# App
app = Flask(__name__)
app.config['SECRET_KEY'] = '1e34128f52ed4465e4be4734ed6b969d'
if os.getenv("DATABASE_URL"):
    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv("DATABASE_URL")
else:
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///comunidade.db'

#Banco de dados
database = SQLAlchemy(app)

#Criptografia das senhas
bcrypt = Bcrypt(app)

#Login Manager
login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'alert-info'

#Routes
from comunidadeimpressionadora import routes
