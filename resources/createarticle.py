from Model import db,User,Article
from flask_restful import Resource
from flask import request,jsonify,make_response
import uuid
import datetime
import jwt
from decorators.User_token import token_required


class ArticlesAPi(Resource):
    
    # @token_required
    def get(self,*args):
        
        def get_paginated_list(results, url, start, limit):
            start = int(start)
            limit = int(limit)
            count = len(results)
            if count < start or limit < 0:
                return {"1":limit,"2":start,"3":count}
                # abort(404)
            
            obj = {}
            obj['start'] = start
            obj['limit'] = limit
            obj['count'] = count
    
            if start == 1:
                obj['previous'] = ''
            else:
                start_copy = max(1, start - limit)
                limit_copy = start - 1
                obj['previous'] = url + '?start=%d&limit=%d' % (start_copy, limit_copy)
       
            if start + limit > count:
                obj['next'] = ''
            else:
                start_copy = start + limit
                obj['next'] = url + '?start=%d&limit=%d' % (start_copy, limit)
       
            obj['data'] = results[(start - 1):(start - 1 + limit)]
            return obj

        latest_article= Article.query.order_by(Article.id.desc()).all()
        article_list=[]
        for i in latest_article:
            temp_obj={
                'title':i.title,
                'Content':i.Content,
                'tags':i.tags,
                'id':i.id,
                'Category':i.Category,
                'image_url':i.image_url,
                'last_updated':str(i.last_updated)
            }
            article_list.append(temp_obj)
        # print(article_list)
        return get_paginated_list(article_list, '/articles',start=request.args.get('start', 1),limit=request.args.get('limit', 5))
    
    @token_required
    def post(self,*args):
        json_data=request.get_json(force=True)
        
        
        newArticle=Article(title=json_data['title'],image_url=json_data['image_url'],Created_by=json_data['Created_by'],Category=json_data['Category'],Content=json_data['Content'])
        db.session.add(newArticle)
        db.session.commit()



        return {"status":"Success","Message":"Article Craeted"},201
