from .modelo import Usuario,Cliente
from . import db

def crear_usuario(identificacion,Nombre_usuario,Apellido_usuario,Cargo,Contraseña,Direccion,Telefono):
    usuario = Usuario(identificacion=identificacion,Nombre_usuario=Nombre_usuario,Apellido_usuario=Apellido_usuario,Cargo=Cargo,Contraseña=Contraseña,Direccion=Direccion,Telefono=Telefono)
    db.session.add(usuario)
    db.session.commit()

def obtener_usuarios():
    return Usuario.query.all()

def obtener_usuario_por_id(usuario_id):
    return Usuario.query.get(usuario_id)

def actualizar_usuario(usuario_id, nombre, apellido,cargo,contraseña,direccion,telefono):
    usuario = Usuario.query.get(usuario_id)
    if usuario:
        usuario.Nombre_usuario = nombre
        usuario.Apellido_usuario = apellido
        usuario.Cargo = cargo
        usuario.Contraseña = contraseña
        usuario.Direccion = direccion
        usuario.Telefono = telefono
        db.session.commit()

def eliminar_usuario(usuario_id):
    usuario = Usuario.query.get(usuario_id)
    if usuario:
        db.session.delete(usuario)
        db.session.commit()

def obtener_clientes():
    cliente = Cliente.query.all()
    return cliente

def obtener_cliente_por_id(cliente_id):
    return Cliente.query.get(cliente_id)

def crear_cliente(identificacion,Nombre_cliente,Apellido_cliente,Correo_Electronico,Direccion,Telefono):
    cliente = Cliente(identificacion=identificacion,Nombre_cliente=Nombre_cliente,Apellido_cliente=Apellido_cliente,Correo_Electronico=Correo_Electronico,Direccion=Direccion,Telefono=Telefono)
    db.session.add(cliente)
    db.session.commit()

def actualizar_cliente(cliente_id, nombre, apellido, correo_electronico, direccion, telefono):
    cliente = Cliente.query.get(cliente_id)
    if cliente:
        cliente.Nombre_cliente = nombre
        cliente.Apellido_cliente = apellido
        cliente.Correo_Electronico = correo_electronico
        cliente.Direccion = direccion
        cliente.Telefono = telefono
        db.session.commit()

def eliminar_cliente(cliente_id):
    cliente = Cliente.query.get(cliente_id)
    if cliente:
        db.session.delete(cliente)
        db.session.commit()