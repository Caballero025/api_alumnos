from flask import Blueprint, request,jsonify
from app import db
from app.models import Alumnos


alu_bp = Blueprint ('alumnos',__name__)


# Endpoint para agregar todos los alumnos
@alu_bp.route('/alumnos', methods=['POST'])

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

