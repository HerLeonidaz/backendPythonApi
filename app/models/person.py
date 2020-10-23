from . import db

class Person(db.Model):
    __tablename__ = 'persons'

    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(50), nullable=False)
    correo = db.Column(db.Text)
    kmcaminados =  db.Column(db.Text, nullable=False)
    FechaCaptura = db.Column(db.DateTime(), nullable=False, default=db.func.current_timestamp())


    @classmethod
    def new(cls, nombre, correo, kmcaminados):
        return Person(nombre=nombre, correo=correo, kmcaminados=kmcaminados)


    def save(self):
        try:
            db.session.add(self)
            db.session.commit()
            
            return True
        except:
            return False


    def __str__(self):
        return self.nombre

    
    def serialize(self):
        return {
            'nombre': self.nombre,
            'correo': self.correo,
            'kmcaminados': self.kmcaminados
        }