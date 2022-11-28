
from flask import Flask,request,jsonify,render_template
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from sqlalchemy import func,case,desc,asc
import datetime as dt
from flask_migrate import Migrate
from dotenv import load_dotenv
import os

app = Flask(__name__)
if os.getenv('GENERAL_DB_TYPE') == 'SQLITE':
    app.config['SQLALCHEMY_DATABASE_URI']=os.getenv('SQLITE_DATABASE_URI')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
elif os.getenv('GENERAL_DB_TYPE') == 'MYSQL':
    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('SQLALCHEMY_DATABASE_URI')
    app.config['MYSQL_USER']=os.getenv('MYSQL_USERNAME')
    app.config['MYSQL_PASSWORD']=os.getenv('MYSQL_PASSWORD')
    app.config['MYSQL_HOST']=os.getenv('MYSQL_SERVER')
    app.config['MYSQL_DB']=os.getenv('MYSQL_DB_NAME')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
     

db = SQLAlchemy(app)
ma = Marshmallow(app)
migrate = Migrate(app,db)

class UserSchema(ma.Schema):
    class Meta:
        fields = ('id','user_name','first_name','last_name','password','full_name','gender_percent','birth_month')

user_schema = UserSchema()
users_schema = UserSchema(many=True)