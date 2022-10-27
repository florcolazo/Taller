from api_config import db

class Proveedor(db.Model):
    __tablename__ = "pago"
    idProveedor = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(20))
    cuit = db.Column(db.Integer)

    idPP = db.Column(db.Integer, db.ForeignKey("proveedor-producto.id"))