from api_config import db

class Pet(db.Model):
    __tablename__ = "pet"
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(50))
    tipo = db.Column(db.String(15))
    raza = db.Column(db.String(15))
    descripcion = db.Column(db.String(140))
    pet_id = db.Column(db.Integer, db.ForeignKey("servicios.id"))

    