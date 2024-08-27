from flask import Blueprint, jsonify, request, render_template
from .controlador import crear_usuario, obtener_usuarios, obtener_usuario_por_id, actualizar_usuario, eliminar_usuario,obtener_clientes,obtener_cliente_por_id,crear_cliente,actualizar_cliente,eliminar_cliente

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

@main_blueprint.route('/clientes', methods=['GET'])
def listar_clientes():
    clientes = obtener_clientes()
    return jsonify([{'id': c.identificacion, 'nombre': c.Nombre_cliente, 'apellido': c.Apellido_cliente, 'correo_electronico': c.Correo_Electronico, 'direccion': c.Direccion, 'telefono': c.Telefono} for c in clientes])

@main_blueprint.route('/clientes/<int:id>', methods=['GET'])
def ver_cliente(id):
    c = obtener_cliente_por_id(id)
    if c:
        return jsonify({'id': c.identificacion, 'nombre': c.Nombre_cliente, 'apellido': c.Apellido_cliente, 'correo_electronico': c.Correo_Electronico, 'direccion': c.Direccion, 'telefono': c.Telefono})
    return jsonify({'error': 'Cliente no encontrado'}), 404

@main_blueprint.route('/clientes', methods=['POST'])
def agregar_cliente():
    data = request.json
    crear_cliente(data['identificacion'], data['Nombre_cliente'], data['Apellido_cliente'], data['Correo_Electronico'], data['Direccion'], data['Telefono'])
    return jsonify({'mensaje': 'Cliente creado exitosamente'}), 201

@main_blueprint.route('/clientes/<int:id>', methods=['PUT'])
def editar_cliente(id):
    data = request.json
    actualizar_cliente(id, data['Nombre_cliente'], data['Apellido_cliente'], data['Correo_Electronico'], data['Direccion'], data['Telefono'])
    return jsonify({'mensaje': 'Cliente actualizado exitosamente'})

@main_blueprint.route('/clientes/<int:id>', methods=['DELETE'])
def borrar_cliente(id):
    cliente = obtener_cliente_por_id(id)
    if cliente:
        eliminar_cliente(id)
        return jsonify({'mensaje': 'Cliente eliminado exitosamente'})
    return jsonify({'mensaje': 'Error, cliente no encontrado'})

