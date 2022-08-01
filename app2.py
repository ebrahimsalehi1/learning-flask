from flask import Flask,request,jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///mydb.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
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

    def get_json(self):
        return {
        "user_name":self.user_name,
        # "password":self.password,
        "first_name":self.first_name,
        "last_name":self.last_name,
        "user_type":self.user_type
        }

@app.route('/adduser',methods=['POST'])
def add_user():
    try:
        body = request.get_json()

        user_obj = {
            "user_name":body['username'],
            "password" :body['password'],
            "first_name":body['firstName'],
            "last_name":body['lastName'],
            "user_type":body['userType']
        }

        new_user = User(user_obj['user_name'],user_obj['password'],user_obj['first_name'],user_obj['last_name'],user_obj['user_type'])
        print(new_user.id)
        db.session.add(new_user)
        db.session.commit()

        return user_obj,200

    except Exception as ex:
        print(ex)
        codes = 100

        return {"message":str(ex)},417

@app.route('/getusers')
def get_users():
    all_users = User.query.all()
    str_result ='['
    i=0
    for user in all_users:
        str_result = str_result+str(user.get_json())
        if i<len(all_users)-1:
            str_result=str_result+","

        i=i+1

    str_result=str_result+']'

    return jsonify(str_result)


@app.route('/edituser',methods=['PUT'])
def edit_user():
    try:
        body = request.get_json()

        user_obj = {
            "user_name":body['username'],
            "password" :body['password'],
            "first_name":body['firstName'],
            "last_name":body['lastName'],
            "user_type":body['userType']
        }

        new_user = User(user_obj['user_name'],user_obj['password'],user_obj['first_name'],user_obj['last_name'],user_obj['user_type'])        
        db.session.commit()

        return user_obj,200

    except Exception as ex:
        print(ex)
        codes = 100

        return {"message":str(ex)},417

@app.route('/deleteuser/<user_id>',methods=['DELETE'])
def delete_user(user_id):
    try:
        found_user = User.query.filter_by(id=user_id).first()
        db.session.delete(found_user)
        db.session.commit()

        return "OK",200

    except Exception as ex:
        print(ex)
        return {"message":str(ex)},404

if __name__=='__main__':
    db.create_all()


    app.run(debug=True)
