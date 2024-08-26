from .modelo import Usuario
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
