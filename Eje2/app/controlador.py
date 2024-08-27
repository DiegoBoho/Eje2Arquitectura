from .modelo import Usuario,Cliente,Productos,Factura,DetalleFactura
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

def listar_productos():
    productos = Productos.query.all()
    return productos

def obtener_productos_por_id(producto_id):
    return Productos.query.get(producto_id)

def crear_productos(id_producto,Nombre_producto,Precio):
    productos = Productos(id_producto = id_producto,Nombre_producto=Nombre_producto,Precio=Precio)
    db.session.add(productos)
    db.session.commit()

def actualizar_productos(producto_id, nombre, precio):
    productos = Productos.query.get(producto_id)
    if productos:
        productos.Nombre_producto = nombre
        productos.Precio = precio
        db.session.commit()

def eliminar_productos(producto_id):
    productos = Productos.query.get(producto_id)
    if productos:
        db.session.delete(productos)
        db.session.commit()

def listar_factura():
    return Factura.query.all()

def obtener_factura_por_id(factura_id):
    return Factura.query.get(factura_id)

def crear_factura(id_Factura,Fecha_Generacion,id_Usuario,id_Cliente):
    facturas = Factura(id_Factura=id_Factura,Fecha_Generacion=Fecha_Generacion,id_Usuario=id_Usuario,id_Cliente=id_Cliente)
    db.session.add(facturas)
    db.session.commit()

def actualizar_factura(factura_id, fecha_generacion,id_Usuario,id_Cliente):
    facturas = Factura.query.get(factura_id)
    if facturas:
        facturas.Fecha_Generacion = fecha_generacion
        facturas.id_Usuario = id_Usuario
        facturas.id_Cliente = id_Cliente
        db.session.commit()

def eliminar_factura(factura_id):
    facturas = Factura.query.get(factura_id)
    if facturas:
        db.session.delete(facturas)
        db.session.commit()

def crear_factura_detalles(id_Detalle_Factura,id_Factura,id_producto,cantidad,precio_total):
    facturas = DetalleFactura(id_Detalle_Factura=id_Detalle_Factura,id_Factura=id_Factura,id_producto=id_producto,cantidad=cantidad,precio_total=precio_total)
    db.session.add(facturas)
    db.session.commit()

def actualizar_factura_detalles(factura_id, id_Factura,id_producto,cantidad,precio_total):
    facturas = DetalleFactura.query.get(factura_id)
    if facturas:
        facturas.id_Factura = id_Factura
        facturas.id_producto = id_producto
        facturas.cantidad = cantidad
        facturas.precio_total = precio_total
        db.session.commit()

def eliminar_factura_detalles(factura_id):
    facturas = DetalleFactura.query.get(factura_id)
    if facturas:
        db.session.delete(facturas)
        db.session.commit() 

def listar_detalles_factura():
    return DetalleFactura.query.all()

def obtener_detalles_factura_por_id(detalles_factura_id):
    return DetalleFactura.query.get(detalles_factura_id)