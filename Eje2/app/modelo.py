from . import db
from datetime import datetime

class Usuario(db.Model):
    __tablename__ = "usuario"
    identificacion = db.Column(db.Integer, primary_key=True, index=True)
    Nombre_usuario = db.Column(db.String(64))
    Apellido_usuario = db.Column(db.String(64))
    Cargo = db.Column(db.String(15))
    Contraseña = db.Column(db.String(10))
    Direccion = db.Column(db.String(40))
    Telefono = db.Column(db.String(15))  # Ajustado a String para mayor flexibilidad

    def __repr__(self):
        return f'<Usuario {self.Nombre_usuario}>'  # Corregido para reflejar la columna correcta

class Cliente(db.Model):
    __tablename__ = "cliente"
    identificacion = db.Column(db.Integer, primary_key=True, index=True)
    Nombre_cliente = db.Column(db.String(64))
    Apellido_cliente = db.Column(db.String(64))
    Correo_Electronico = db.Column(db.String(120))  # Ajustado para almacenar correos electrónicos completos
    Direccion = db.Column(db.String(40))
    Telefono = db.Column(db.Integer)  # Ajustado a String para mayor flexibilidad

    def __repr__(self):
        return f'<Cliente {self.Nombre_cliente}>'  # Corregido para reflejar la columna correcta

class Productos(db.Model):
    __tablename__ = "productos"
    id_producto = db.Column(db.Integer, primary_key=True, index=True)
    Nombre_producto = db.Column(db.String(64))
    Precio = db.Column(db.Integer)

    def __repr__(self):
        return f'<Productos {self.Nombre_producto}>'  # Corregido para reflejar la columna correcta

class Factura(db.Model):
    __tablename__ = "factura"
    id_Factura = db.Column(db.Integer, primary_key=True, index=True)
    Fecha_Generacion = db.Column(db.DateTime, default=datetime.utcnow)  # Corregido db.Datetime a db.DateTime
    id_Usuario = db.Column(db.Integer, db.ForeignKey('usuario.identificacion'))  # Corregido Usuario a usuario
    id_Cliente = db.Column(db.Integer, db.ForeignKey('cliente.identificacion'))  # Corregido Cliente a cliente

    detalles = db.relationship('DetalleFactura', backref='factura', lazy=True)

    def __repr__(self):
        return f'<Factura {self.id_Factura}>'  # Corregido para reflejar la columna correcta

class DetalleFactura(db.Model):
    __tablename__ = 'detalle_factura'
    id_Detalle_Factura = db.Column(db.Integer, primary_key=True, index=True)
    id_producto = db.Column(db.Integer, db.ForeignKey('productos.id_producto'))  # Corregido Productos a productos
    cantidad = db.Column(db.Integer)
    precio_total = db.Column(db.Integer)
    id_Factura = db.Column(db.Integer, db.ForeignKey('factura.id_Factura'))  # Corregido Factura a factura

    def __repr__(self):
        return f'<DetalleFactura {self.id_Detalle_Factura}>'
