from api_config import db

class Proveedor-Producto(db.Model):
    __tablename__ = "pago"
    idPP = db.Column(db.Integer, primary_key=True)
    costo = db.Column(db.float)
    cantidad = db.Column(db.Integer)

