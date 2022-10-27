from api_config import db

class Pago(db.Model):
    __tablename__ = "pago"
    idPago = db.Column(db.Integer, primary_key=True)
    fecha = db.Column(db.Date)
    
    
    idFactura = db.Column(db.Integer, db.ForeignKey("factura.id"))
   