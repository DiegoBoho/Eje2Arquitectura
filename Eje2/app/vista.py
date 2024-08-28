from flask import Blueprint, jsonify, request, render_template
from .controlador import crear_usuario, obtener_usuarios, obtener_usuario_por_id, actualizar_usuario, eliminar_usuario
from .controlador import obtener_clientes,obtener_cliente_por_id,crear_cliente,actualizar_cliente,eliminar_cliente
from .controlador import listar_productos,crear_productos,obtener_productos_por_id,actualizar_productos,eliminar_productos
from .controlador import crear_factura,listar_factura,obtener_factura_por_id,actualizar_factura,eliminar_factura
from .controlador import crear_factura_detalles,listar_detalles_factura,actualizar_factura_detalles,eliminar_factura_detalles,obtener_detalles_factura_por_id

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


@main_blueprint.route('/productos',methods=['GET'])
def lista_productos():
    productos = listar_productos()
    return jsonify([{'id_producto':u.id_producto,'Nombre_producto':u.Nombre_producto,'precio':u.Precio}for u in productos])

@main_blueprint.route('/productos/<int:id>', methods=['GET'])
def obtener_producto_id(id):
    p = obtener_productos_por_id(id)
    return jsonify({'id_producto':p.id_producto,'Nombre_producto':p.Nombre_producto,'Precio':p.Precio})

@main_blueprint.route('/productos', methods=['POST'])
def crear_producto():
    data = request.json
    crear_productos(data['id_producto'], data['Nombre_producto'], data['Precio'])
    return jsonify({'mensaje': 'Producto creado exitosamente'}), 201 
   
@main_blueprint.route('/productos/<int:id>', methods=['PUT'])
def actualizar_producto(id):
    data = request.json
    actualizar_productos(id, data['Nombre_producto'], data['Precio'])
    return jsonify({'mensaje': 'Producto actualizado exitosamente'})

@main_blueprint.route('/productos/<int:id>', methods=['DELETE'])
def borrar_productos(id):
    productos = obtener_productos_por_id(id)
    if productos:
        eliminar_productos(id)
        return jsonify({'mensaje': 'Producto eliminado exitosamente'})
    return jsonify({'mensaje': 'Error, producto no encontrado'})

@main_blueprint.route('/facturas',methods=['GET'])
def lista_facturas():
    facturas = listar_factura()
    return jsonify([{'id_Factura':u.id_Factura,'Fecha_Generacion':u.Fecha_Generacion,'id_Usuario':u.id_Usuario,'id_Cliente':u.id_Cliente}for u in facturas])

@main_blueprint.route('/facturas/<int:id>', methods=['GET'])
def obtener_factura_id(id):
    p = obtener_factura_por_id(id)
    return jsonify({'id_Factura':p.id_Factura,'Fecha_Generacion':p.Fecha_Generacion,'id_Usuario':p.id_Usuario,'id_Cliente':p.id_Cliente})

@main_blueprint.route('/facturas', methods=['POST'])
def crear_facturas():
    data = request.json
    crear_factura(data['id_factura'], data['Fecha_generacion'], data['id_Usuario'], data['id_Cliente'])
    return jsonify({'mensaje': 'Factura creado exitosamente'}), 201

@main_blueprint.route('/facturas/<int:id>', methods=['PUT'])
def actualizar_factura(id):
    data = request.json
    actualizar_factura(id, data['Fecha_generacion'], data['id_Usuario'], data['id_Cliente'])
    return jsonify({'mensaje': 'Factura actualizado exitosamente'})

@main_blueprint.route('/facturas/<int:id>', methods=['DELETE'])
def borrar_factura(id):
    facturas = obtener_factura_por_id(id)
    if facturas:
        eliminar_factura(id)
        return jsonify({'mensaje': 'Factura eliminado exitosamente'})
    return jsonify({'mensaje': 'Error, Factura no encontrado'})

@main_blueprint.route('/facturasdetalles/<int:id>', methods=['GET'])
def obtener_factura_detalles(id):
    p = obtener_detalles_factura_por_id(id)
    return jsonify({'id_detalle_factura':p.id_Detalle_Factura,'id_producto':p.id_producto,'cantidad':p.cantidad,'precio_total':p.precio_total,'id_Factura':p.id_Factura})

@main_blueprint.route('/facturasdetalles', methods=['GET'])
def lista_factura_detalles():
    lf = listar_detalles_factura()
    return jsonify([{'id_Detalle_Factura':u.id_Detalle_Factura,'id_producto':u.id_producto,'cantidad':u.cantidad,'precio_total':u.precio_total,'id_Factura':u.id_Factura}for u in lf])

@main_blueprint.route('/facturasdetalles', methods=['POST'])
def crear_factura_detalle():
    data = request.json
    crear_factura_detalles(data['id_Detalle_Factura'], data['id_producto'], data['cantidad'], data['precio_total'], data['id_Factura'])
    return jsonify({'mensaje': 'Factura Detalle creado exitosamente'}), 201

@main_blueprint.route('/facturasdetalles/<int:id>', methods=['PUT'])
def editar_factura_detalle(id):
    data = request.json
    actualizar_factura_detalles(id, data['id_Factura'], data['id_producto'], data['cantidad'], data['precio_total'])
    return jsonify({'mensaje': 'Factura Detalle actualizado exitosamente'})

@main_blueprint.route('/facturasdetalles/<int:id>', methods=['DELETE'])
def borrar_factura_detalles(id):
    facturas = obtener_productos_por_id(id)
    if facturas:
        eliminar_factura_detalles(id)
        return jsonify({'mensaje': 'Factura Detalle eliminado exitosamente'})
    return jsonify({'mensaje': 'Error, Factura Detalle no encontrado'})
