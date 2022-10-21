from api_config import db


class Product(db.Model):
    __tablename__ = "product"
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(50))
    categoria = db.Column(db.String(70))
    precio = db.Column(db.float)
    stock = db.Column(db.Int)
    descripcion = db.Column(db.String(140))
    product_id = db.Column(db.Integer, db.ForeignKey("proveedor-producto.id"))
    product_id = db.Column(db.Integer, db.ForeignKey("detalle-carrito.id"))
    product_id = db.Column(db.Integer, db.ForeignKey("preguntas.id"))