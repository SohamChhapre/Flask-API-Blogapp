from flask import Flask
from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
ma = Marshmallow()
db = SQLAlchemy()


class User(db.Model):
    __tablename__='user'
    id=db.Column(db.String(20), primary_key=True)
    name=db.Column(db.String(40), nullable=False)
    password=db.Column(db.String(85),nullable=False)
    public_id=db.Column(db.String(50),default='123')


    def __init__self(self,id,name,password,public_id):
        self.id=id
        self.name=name
        self.password=password
        self.public_id=public_id


class Article(db.Model):
    __tablename__="Article"
    id=db.Column(db.Integer,primary_key=True )
    title=db.Column(db.String(300),nullable=False)
    image_url=db.Column(db.String(300),nullable=False)
    Created_by=db.Column(db.String(50),nullable=False)
    Category=db.Column(db.String(50),nullable=False)
    tags=db.Column(db.String(300), default="notags")
    Content=db.Column(db.Text)
    last_updated=db.Column(db.DateTime, nullable=False,default=datetime.utcnow())
    


    def __init__self(self,title,image_url,Created_by,Category,Content):
        self.title=title
        self.image_url=image_url
        self.Created_by=Created_by
        # self.last_updated=last_updated
        self.Content=Content
        self.Category=Category
