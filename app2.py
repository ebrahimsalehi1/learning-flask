from enum import unique
from flask import Flask,request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///mydb.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

    #   "userId": 100,
    #   "username": "ebrahim2000",
    #   "password": "1234",
    #   "firstName": "ebrahim",
    #   "lastName": "salehi",
    #   "userType": "teacher"

class User(db.Model):
    id=db.Column("user_id",db.Integer,primary_key=True)
    user_name = db.Column(db.String(50),unique=True)
    password = db.Column(db.String(12),nullable=False)
    first_name = db.Column(db.String(50),nullable=False)
    last_name = db.Column(db.String(50),nullable=False)
    user_type = db.Column(db.String(50),nullable=False)



    def __init__(self,user_name,password,first_name,last_name,user_type):
        self.user_name=user_name
        self.password=password
        self.first_name=first_name
        self.last_name=last_name
        self.user_type=user_type


@app.route('/adduser',methods=['POST'])
def add_user():
    try:
        body = request.get_json()

        user_name=body['username']
        password=body['password']
        first_name=body['firstName']
        last_name=body['lastName']
        user_type=body['userType']

        new_user = User(user_name,password,first_name,last_name,user_type)
        db.session.add(new_user)
        db.session.commit()

        return "True"

    except Exception as ex:
        print(ex)
        return "False"

if __name__=='__main__':
    db.create_all()


    app.run(debug=True)
