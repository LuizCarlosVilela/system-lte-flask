from flask.config import Config
from config import bd

class Usuario(bd.Model):
    __tablename__ = 'usuarios'
    id = bd.Column(bd.Integer, primary_key=True)
    nome = bd.Column(bd.String(256))
    email = bd.Column(bd.String(128), unique=True)

    def __init__(self, nome, email):
        self.nome = nome
        self.email = email

    def __repr__(self):
        return '<Usuário com ID = ' + str(self.id) + '>'