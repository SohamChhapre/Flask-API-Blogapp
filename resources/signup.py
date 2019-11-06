from flask import request,jsonify
from flask_restful import Resource
# from run import app
from Model import db,User
from werkzeug.security import generate_password_hash
import uuid
import datetime
import jwt
from decorators.User_token import token_required

class SignupApi(Resource):
    # @token_required
    def get(self,*args,**kwargs):
        Userdata = db.session.query(User)
        query=Userdata.all()
        user_list=[]
        for i in query:
            temp_obj={
                'id':i.id,
                'name':i.name,
                'password':i.password
            }
            user_list.append(temp_obj)

        return {"status":"success",'data': user_list},200


    def post(self,*args):
        #auth=request.authorization
        json_data=request.get_json(force=True)
        # json_data=auth
        if not json_data:
            return {'message':'No input data provided'},400
        preuser=User.query.filter_by(id=json_data['id']).first()
        if preuser:
            return {'message':'email already exist'},400
        user={'name':json_data['name'],'email':json_data['id']}
        encrpted_pass=generate_password_hash(json_data['password'],method='sha256')
        encrpted_public_id=str(uuid.uuid4())
        newuser=User(
            id=json_data['id'],
            name=json_data['name'],
            password=encrpted_pass,
            public_id=encrpted_public_id
        )
        token=jwt.encode({'public_id':newuser.public_id,'exp':datetime.datetime.utcnow()+datetime.timedelta(minutes=45)},'Elegance-1234')
        db.session.add(newuser)
        db.session.commit()


        return  {"message":"Success","data":user,"token":token.decode('UTF-8'),'create': "User is added"}, 201

    def delete(self):
        Userdata = db.session.query(User)
        query = Userdata.all()
        for i in query:
            db.session.delete(i)
        db.session.commit()
        return jsonify({'message':'deleted'})


