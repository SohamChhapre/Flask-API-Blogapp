from Model import db,User,Article
from flask_restful import Resource
from flask import request,jsonify,make_response
import uuid
import datetime
import jwt
from decorators.User_token import token_required
import json

class ArticleAPi(Resource):
    
    def get(self,id,*args):
        # print(id,len(args))
        article = db.session.query(Article)
        query=article.filter_by(id=id).first()
        # for i in query:
        temp_obj={
            'id':query.id,
            'Category':query.Category,
            'title':query.title,
            'Created_by':query.Created_by,
            'image_url':query.image_url,
            'last_updated':str(query.last_updated)
        }
        print(temp_obj)
        
        return temp_obj

    
    
        
    
    def delete(self,id,*args):
        article = Article.query.filter_by(id=id).delete()
        db.session.commit()    
        return {"message":'article deleted succesfully'},200