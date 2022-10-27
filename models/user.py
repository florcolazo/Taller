from api_config import db


class User(db.Model):
    __tablename__ = "user"
    dni = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(20))
    apellido = db.Column(db.String(20))
    telefono = db.Column(db.Integer)
    correoelectronico = db.Column(db.String(20))
    domicilio = db.Column(db.String(20))
    beneficiario = db.Column(db.boolean)
    tipo = db.Column(db.boolean)


    
    user = db.relationship("Usuario")
    idFactura = db.Column(db.Integer, db.ForeignKey("factura.id"))
    idMascota = db.Column(db.Integer, db.ForeignKey("pet.id"))
    idPreguntas = db.Column(db.Integer, db.ForeignKey("preguntas.id"))
    
