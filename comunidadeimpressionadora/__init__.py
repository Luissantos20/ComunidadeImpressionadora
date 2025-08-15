from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
import os

# Configuração do app
app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'chave_default_secreta')

# Configuração do banco de dados
database_url = os.getenv("DATABASE_URL")
if database_url:
    app.config['SQLALCHEMY_DATABASE_URI'] = database_url
else:
    # fallback para SQLite local, útil para desenvolvimento
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///comunidade.db'

# Inicialização das extensões
database = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'alert-info'

# Importa modelos e rotas
from comunidadeimpressionadora import models, routes

# Cria tabelas que ainda não existem (não apaga dados)
with app.app_context():
    database.create_all()
    print("Tabelas criadas (somente se não existiam)")
