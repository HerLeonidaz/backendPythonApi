from flask import jsonify

def bad_request():
    return jsonify({
        'success': False,
        'data':{},
        'messages':'Bad request',
        'code':400
    }), 400
    
def response(data):
    return jsonify({
        'success':True,
        'data': data
    }),200
