from flask import Blueprint,request,jsonify,make_response
from database import Query
from utils import JwtBuilder,verify
from app.v1.data_models import FoodResponse
from utils import is_authorize

v1_bp = Blueprint('v1', __name__)

@v1_bp.route('/',methods=['GET'])
def v1_root():
    return {"message":"running..."}

@v1_bp.route('/register',methods=['POST'])
def v1_register():
    try:
        user_data = request.json 
        token=Query.register(
            name=user_data.get('name'),
            email=user_data.get('email'),
            password=user_data.get('password')
        )
        return make_response(jsonify({"message":"registered successfully!","token":token}),201)
    except Exception as e:
        return make_response(jsonify({"message":str(e)}),500)
    

@v1_bp.route('/login',methods=['POST'])
def v1_login():
    try:
        login_data = request.json 
        user=Query.getUser(
            email=login_data.get('email')
        )
        if not user:
            return make_response(jsonify({"message":"user does not exists!"}),400)
        
        user=user[0]
        password=user[3]

        if not verify(login_data.get('password'),password):
            return make_response(jsonify({"message":"wrong password!"}),400)

        payload={"name":user[1],"sub":login_data.get('email')}
        token=JwtBuilder(payload=payload).get_token()
        
        return make_response(jsonify({"message":"logged in successfully!","token":token}),200)
    except Exception as e:
        return make_response(jsonify({"message":str(e)}),500)
    

@v1_bp.route('/get-recipe',methods=['POST'])
@is_authorize
def v1_recipe():
    try:
        data = request.json 
        dishes=Query.get_foods(
            dish_name=data.get('dish_name')
        )
        res=FoodResponse(dishes).toJson()
        return make_response(jsonify({"recipe":res}),200)
    except Exception as e:
        return make_response(jsonify({"message":str(e)}),500)
    
@v1_bp.route('/recipe',methods=['POST'])
def v1_recipe2():
    try:
        data = request.json 
        dishes=Query.get_foods(
            dish_name=data.get('dish_name')
        )
        res=FoodResponse(dishes).toJson()
        return make_response(jsonify({"recipe":res}),200)
    except Exception as e:
        return make_response(jsonify({"message":str(e)}),500)