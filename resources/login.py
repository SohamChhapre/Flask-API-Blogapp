from flask import request,jsonify,make_response
from flask_restful import Resource
from Model import db,User
from werkzeug.security import generate_password_hash,check_password_hash
import uuid
import datetime
import jwt
from decorators.User_token import token_required

class LoginApi(Resource):
    @token_required
    def get(self, *args, **kwargs):
        Userdata = db.session.query(User)
        query = Userdata.all()
        user_list = []
        for i in query:
            temp_obj = {
                'id': i.id,
                'name': i.name,
                'password': i.password
            }
            user_list.append(temp_obj)

        return {"status": "success", 'data': user_list}, 200

    def post(self,*args):

        json_data=request.get_json(force=True)

        if not json_data:
            return {"message":"Request body missing","status":"Failure"},401

        user=User.query.filter_by(id=json_data['id']).first()
        if not user:
            return {"message":"User not Exists","status":"Failure"},400

        elif not check_password_hash(user.password,json_data['password']):
            return {"message":"Invalid password","status":"Failure"},401
     
        else:
            data={"name":user.name,"id":user.id}
            token = jwt.encode(
                {'public_id': user.public_id, 'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=45)}, 'Elegance-1234')

            return {"data":data,"token":token.decode('UTF-8'),"status":"Success"},200






