from api_config import db

class Respuestas(db.Model):
    __tablename__ = "pago"
    idRespuestas = db.Column(db.Integer, primary_key=True)
    descripcion = db.Column(db.String(30))
    
