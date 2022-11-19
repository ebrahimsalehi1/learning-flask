from flask import Flask,request,jsonify,render_template
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from sqlalchemy import func,case,desc,asc
import datetime as dt
from flask_migrate import Migrate
from init import db

class User(db.Model):
    id=db.Column(db.Integer,primary_key=True,autoincrement=True)
    user_name = db.Column(db.String(50),unique=True)
    password = db.Column(db.String(12),nullable=False)
    first_name = db.Column(db.String(50),nullable=False)
    last_name = db.Column(db.String(50),nullable=False)
    birth_date = db.Column(db.Date,nullable=True)
    usertype_id = db.Column(db.Integer,db.ForeignKey('usertype.id'))
    gender_id = db.Column(db.Integer,db.ForeignKey('gender.id'))
    # eye_color = db.Column(db.String(30))
    full_name = db.column_property(first_name+' '+last_name)
    gender_percent = db.column_property(case([(gender_id==1,1.25),(gender_id==2,1.15)]))
    birth_month = db.column_property(func.extract('month',birth_date))
    image = db.Column(db.BLOB)

    def __init__(self,user_name,password,first_name,last_name,birth_date,usertype_id,gender_id):
        self.user_name=user_name
        self.password=password
        self.first_name=first_name
        self.last_name=last_name
        self.birth_date=birth_date
        self.usertype_id=usertype_id
        self.gender_id=gender_id
        # self.eye_color=eye_color

    def get_json(self):
        return {
        "user_name":self.user_name,
        # "password":self.password,
        "first_name":self.first_name,
        "last_name":self.last_name,
        "user_type":self.user_type
        }

    @property
    def first_name_search(self):
        return self.first_name.upper()