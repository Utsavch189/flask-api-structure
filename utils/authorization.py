from utils import JwtBuilder
from flask import request, jsonify,make_response

def is_authorize(func):
    def wrapper(*args, **kwargs):
        if not request.headers.get('Authorization'):
            return make_response(jsonify({"message": "Authorization token is missing"}), 401)
        
        auth_token = request.headers.get('Authorization').split(" ")[1]

        if not JwtBuilder(token=auth_token).decode():
            return make_response(jsonify({"message": "Authorization token is invalid"}), 401)
        
        return func(*args,**kwargs)
    return wrapper