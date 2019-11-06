from flask import Blueprint
from  flask_restful import Api

from resources.signup import SignupApi
from resources.login import LoginApi
from resources.createarticle import ArticlesAPi
from resources.article import ArticleAPi
from resources.Userarticle import UserArticleAPi
api_bp=Blueprint('api',__name__)
api=Api(api_bp)



api.add_resource(SignupApi,'/signup')

api.add_resource(LoginApi,'/login')

api.add_resource(ArticlesAPi,'/articles')

api.add_resource(ArticleAPi,'/article/<int:id>')

api.add_resource(UserArticleAPi,'/article/<string:username>')