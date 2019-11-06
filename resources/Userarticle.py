from flask_restful import Resource
from Model import db,User,Article
from flask_restful import Resource
from flask import request,jsonify,make_response
import uuid
import datetime
import jwt
from decorators.User_token import token_required
import json

class UserArticleAPi(Resource):
    
    
    
    def get(self,username,*args):
        article=Article.query.filter_by(Created_by=username)
        data=[]
        for query in article:
            temp_obj={
            'id':query.id,
            'Category':query.Category,
            'title':query.title,
            'Created_by':query.Created_by,
            'image_url':query.image_url,
            'last_updated':str(query.last_updated)
             }
            data.append(temp_obj)
      
        return {"data":data,"message":"Success"},200