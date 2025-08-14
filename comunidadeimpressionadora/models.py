from comunidadeimpressionadora import database, login_manager
from datetime import datetime, timezone
from flask_login import UserMixin

@login_manager.user_loader
def load_usuario(id_usuario):
    return Usuario.query.get(int(id_usuario))

# Criar tabelas
class Usuario(database.Model, UserMixin):
    id_usuario = database.Column(database.Integer, primary_key=True)
    username =  database.Column(database.String, nullable=False)
    email = database.Column(database.String, nullable=False, unique=True)
    senha = database.Column(database.String, nullable=False)
    foto_perfil = database.Column(database.String, default='default.jpg')
    posts = database.relationship('Post', backref='autor', lazy=True)
    cursos = database.Column(database.String, nullable=False, default='Não Informado')

    def get_id(self):
        return str(self.id_usuario)
    
    def contar_posts(self):
        return len(self.posts)

class Post(database.Model):
    id_post = database.Column(database.Integer, primary_key=True)
    titulo = database.Column(database.String, nullable=False)
    corpo = database.Column(database.Text, nullable=False)
    data_criacao = database.Column(database.DateTime, nullable=False, default=lambda: datetime.now(timezone.utc))
    id_usuario = database.Column(database.Integer, database.ForeignKey('usuario.id_usuario'), nullable=False)
