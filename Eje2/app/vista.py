from flask import Blueprint, jsonify, request, render_template
from .controlador import crear_usuario, obtener_usuarios, obtener_usuario_por_id, actualizar_usuario, eliminar_usuario

main_blueprint = Blueprint('main', __name__)

@main_blueprint.route('/inicioaplicacion')
def index():
    return render_template('index.html')

@main_blueprint.route('/usuarios', methods=['GET'])
def listar_usuarios():
    usuarios = obtener_usuarios()
    return jsonify([{'id': u.identificacion, 'nombre': u.Nombre_usuario, 'apellido': u.Apellido_usuario, 'cargo': u.Cargo, 'contraseña': u.Contraseña, 'direccion': u.Direccion, 'telefono': u.Telefono} for u in usuarios])

@main_blueprint.route('/usuarios/<int:id>', methods=['GET'])
def ver_usuario(id):
    u = obtener_usuario_por_id(id)
    if u:
        return jsonify({'id': u.identificacion, 'nombre': u.Nombre_usuario, 'apellido': u.Apellido_usuario, 'cargo': u.Cargo, 'contraseña': u.Contraseña, 'direccion': u.Direccion, 'telefono': u.Telefono})
    return jsonify({'error': 'Usuario no encontrado'}), 404

@main_blueprint.route('/usuarios', methods=['POST'])
def agregar_usuario():
    data = request.json
    crear_usuario(data['identificacion'], data['Nombre_usuario'], data['Apellido_usuario'], data['Cargo'], data['Contraseña'], data['Direccion'], data['Telefono'])
    return jsonify({'mensaje': 'Usuario creado exitosamente'}), 201

@main_blueprint.route('/usuarios/<int:id>', methods=['PUT'])
def editar_usuario(id):
    data = request.json
    actualizar_usuario(id, data['Nombre_usuario'], data['Apellido_usuario'], data['Cargo'], data['Contraseña'], data['Direccion'], data['Telefono'])
    return jsonify({'mensaje': 'Usuario actualizado exitosamente'})

@main_blueprint.route('/usuarios/<int:id>', methods=['DELETE'])
def borrar_usuario(id):
    usuario = obtener_usuario_por_id(id)
    if usuario:
        eliminar_usuario(id)
        return jsonify({'mensaje': 'Usuario eliminado exitosamente'})
    return jsonify({'mensaje': 'Error, usuario no encontrado'})