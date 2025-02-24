import os
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv

# Cargar las variables de entorno
load_dotenv()

# Crear instancia de Flask
app = Flask(__name__)

# Configuración de la base de datos PostgreSQL
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Inicializar SQLAlchemy
db = SQLAlchemy(app)

# Modelo de base de datos
class Alumnos(db.Model):
    __tablename__ = 'alumnos'
    no_control = db.Column(db.String, primary_key=True)
    nombre = db.Column(db.String)
    ap_paterno = db.Column(db.String)
    ap_materno = db.Column(db.String)
    semestre = db.Column(db.Integer)

# Endpoint para obtener todos los alumnos
@app.route('/alumnos', methods=['GET'])
def get_alumnos():
    alumnos = Alumnos.query.all()
    lista_alumnos = []
    for alumno in alumnos:  # Cambié `alumnos` por `alumno` dentro del bucle
        lista_alumnos.append({
            'no_control': alumno.no_control,
            'nombre': alumno.nombre,
            'ap_paterno': alumno.ap_paterno,
            'ap_materno': alumno.ap_materno,
            'semestre': alumno.semestre
        })
    return jsonify(lista_alumnos)

# Endpoint para agregar todos los alumnos
@app.route('/alumnos', methods=['POST'])

def insert_alumno():
    data = request.get_json()
    nuevo_alumno = Alumnos(
        no_control = data['no_control'],
        nombre = data['nombre'],
        ap_paterno = data['ap_paterno'],
        ap_materno = data['ap_materno'],
        semestre = data['semestre']
    )
    db.session.add(nuevo_alumno)
    db.session.commit()
    return jsonify ({'msg':'Alumno agregado correctamente'})
# Endpoint para obtener un alumno por el numero de control
@app.route('/alumnos/<no_control>', methods=['GET'])
def get_alumno(no_control):
    alumno = Alumnos.query.get(no_control)
    if alumno is None:
        return jsonify ({'msg':'Alumno no encontrado'})
    return jsonify({
        'no_control':alumno.no_control,
        'nombre':alumno.nombre,
        'ap_paterno':alumno.ap_paterno,
        'ap_materno':alumno.ap_materno,
        'semestre':alumno.semestre,
    })

# Endpoint para eliminar un alumno
@app.route('/alumnos/<no_control>', methods=['DELETE'])
def delete_alumno(no_control):
    alumno = Alumnos.query.get(no_control)
    if alumno is None:
        return jsonify ({'msg':'Alumno no encontrado'})
    db.session.delete(alumno)
    db.session.commit()
    return jsonify({'msg':'Alumno eliminado correctamente'})


# Endpoint para actualizar un alumno
@app.route('/alumnos/<no_control>', methods=['PATCH'])
def update_alumno(no_control):
    alumno = Alumnos.query.get(no_control)
    if alumno is None:
        return jsonify ({'msg':'Alumno no encontrado'})
    data = request.get_json()

    if 'nombre' in data:
        alumno.nombre = data['nombre']
    if 'ap_paterno' in data:
        alumno.ap_paterno = data['ap_paterno']
    if 'ap_materno' in data:
        alumno.ap_materno = data['ap_materno']
    if 'semestre' in data:
        alumno.semestre = data['semestre']

    db.session.commit()
    return jsonify({'msg':'Alumno actualizado correctamente'})

# Endpoint para actualizar todos los datos de un alumno
@app.route('/alumnos/<no_control>', methods=['PUT'])
def updateCom_alumno(no_control):
    alumno = Alumnos.query.get(no_control)
    if alumno is None:
        return jsonify ({'msg':'Alumno no encontrado'})
    data = request.get_json()
    if 'nombre' in data and 'ap_paterno' in data and 'ap_materno' in data and 'semestre' in data:
        alumno.nombre = data['nombre']
        alumno.ap_paterno = data['ap_paterno']
        alumno.ap_materno = data['ap_materno']
        alumno.semestre = data['semestre']
    else: 
        return jsonify({'msg':'DatoS del alumno incompletos'})
    db.session.commit()
    return jsonify({'msg':'Alumno actualizado correctamente'})

    

if __name__ == '__main__':
    app.run(debug=True)
