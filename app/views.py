
from flask import request
from flask import Blueprint

from .models.person import Person
from .responses import response 
from .responses import bad_request

api_v1 = Blueprint('api',__name__,url_prefix='/api/v1')
#endpoint ejercicio 2
@api_v1.route('/persons', methods=['GET'])
def get_persons():
    persons = Person.query.all()
    return response([person.serialize() for person in persons])
#endpoint ejercicio 1
@api_v1.route('/persons', methods=['POST'])
def create_person():
    json = request.get_json(force=True)
    #Condiciones de validación
    if json.get('nombre') is None or len(json['nombre']) > 50:
        return bad_request()
    
    if json.get('correo') is None or len(json['correo']) > 60:
        return bad_request()
    
    if json.get('kmcaminados') is None:
        return bad_request()
    
    #Esta condicion es para validar el número de kilometros
    if int(json.get('kmcaminados')) < 4 :
        return response({'message':'Debes de caminar más'}) 
    
    #
    person = Person.new(json['nombre'], json['correo'], json['kmcaminados'])
    if person.save():
        return response(person.serialize())

    
    return bad_request()

    
    