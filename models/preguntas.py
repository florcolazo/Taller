from api_config import db

class Preguntas(db.Model):
    __tablename__ = "pago"
    idPreguntas = db.Column(db.Integer, primary_key=True)
    descripcion = db.Column(db.String(30))
    estado = db.Column(db.boolean)
