from extensions import db

class Contacto(db.Model):
    __tablename__ = 'contactos'

    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(255), nullable=False)
    telefono = db.Column(db.String(15), nullable=False, unique=True)
    direccion = db.Column(db.String(255))
    email = db.Column(db.String(255))