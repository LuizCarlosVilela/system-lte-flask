from flask import render_template, request, Blueprint
from config import bd
from model.usuario import Usuario

TEMPLATES = './view'
STATIC = './static'

usuario_blueprint = Blueprint('usuarios', __name__, template_folder=TEMPLATES, static_folder=STATIC)

@usuario_blueprint.route('/salvarUsuario', methods=['POST'])
def salvarUsuario():
    email = request.form.get('email')
    nome = request.form.get('nome')

    usuario = Usuario(nome, email)
    bd.session.add(usuario)
    bd.session.commit()
    return 'Ok, usuário salvo!'

@usuario_blueprint.route('/consultarUsuario')
def consultarUsuario():
    usuario_01 = bd.session.query(Usuario).get(1)
    return 'Usuário com ID = ' + str(usuario_01.id) + '; Nome = ' + usuario_01.nome + '.'

@usuario_blueprint.route('/consultarUsuarios')
def consultarUsuarios():
    usuarios = Usuario.query.all()
    return render_template('listarUsuarios.html', usuarios=usuarios)