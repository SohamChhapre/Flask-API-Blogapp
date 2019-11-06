import requests
from flask import jsonify,request
from functools import wraps
# from run import app.config['SECRET_KEY']
from Model import *
import jwt

def token_required(f):
    @wraps(f)
    def decorated(*args,**kwargs):
        token=None

        if 'Authorization' in request.headers:
            token=request.headers['Authorization']
            token = str.replace(str(token), 'Bearer ','')
            # print(token)

        if not token:
            return {'message':'token required'},401
        try:
            data=jwt.decode(token,'Elegance-1234')
            
            curr_user=User.query.filter_by(public_id=data['public_id']).first()
            

        except:
            return {'message':'Invalid token'},401

        return f(curr_user.id,*args,**kwargs)
    return decorated

# def authorize(f):
#     @wraps(f)
#     def decorated_function(*args, **kws):
#             if not 'Authorization' in request.headers:
#                abort(401)

#             user = None
#             data = request.headers['Authorization'].encode('ascii','ignore')
#             token = str.replace(str(data), 'Bearer ','')
#             try:
#                 user = jwt.decode(token, JWT_SECRET, algorithms=['HS256'])['sub']
#             except:
#                 abort(401)

#             return f(user, *args, **kws)            
#     return decorated_function

