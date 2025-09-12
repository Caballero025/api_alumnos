from app import db

class Alumnos(db.Model):
    __tablename__ = 'alumnos'
    no_control = db.Column(db.String, primary_key=True)
    nombre = db.Column(db.String)
    ap_paterno = db.Column(db.String)
    ap_materno = db.Column(db.String)
    semestre = db.Column(db.Integer)

    def to_dict(self):
        return{
            'no_control':self.no_control,
            'nombre':self.nombre,
            'ap_paterno':self.ap_paterno,
            'ap_materno':self.ap_materno,
            'semestre':self.semestre,
        }