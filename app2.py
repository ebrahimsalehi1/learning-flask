from linecache import lazycache
from flask import Flask,request,jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///mydb.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
ma = Marshmallow(app)

class Usertype(db.Model):
    id=db.Column(db.Integer,primary_key=True,autoincrement=True)
    title = db.Column(db.String,unique=True)
    users = db.relationship('User',backref='usertype',lazy=True)

    def __init__(self,title):
        self.title=title

class Gender(db.Model):
    id=db.Column(db.Integer,primary_key=True,autoincrement=True)
    title = db.Column(db.String,unique=True)
    users = db.relationship('User',backref='gender',lazy=True)

    def __init__(self,title):
        self.title=title
class User(db.Model):
    id=db.Column(db.Integer,primary_key=True,autoincrement=True)
    user_name = db.Column(db.String(50),unique=True)
    password = db.Column(db.String(12),nullable=False)
    first_name = db.Column(db.String(50),nullable=False)
    last_name = db.Column(db.String(50),nullable=False)
    usertype_id = db.Column(db.Integer,db.ForeignKey('usertype.id'))
    gender_id = db.Column(db.Integer,db.ForeignKey('gender.id'))

    def __init__(self,user_name,password,first_name,last_name,usertype_id,gender_id):
        self.user_name=user_name
        self.password=password
        self.first_name=first_name
        self.last_name=last_name
        self.usertype_id=usertype_id
        self.gender_id=gender_id

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
       

class UserSchema(ma.Schema):
    class Meta:
        fields = ('id','user_name','first_name','last_name','password')

user_schema = UserSchema()
users_schema = UserSchema(many=True)

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

@app.route('/getusers2')
def get_users2():
    all_users = User.query.all()
    result =users_schema.dump(all_users)

    return jsonify(result)

@app.route('/getuser/<user_id>')
def get_users_by_id(user_id):
    found_user = User.query.get(user_id)
    print(found_user.first_name,found_user.first_name_search)
    result = user_schema.dump(found_user)
    return jsonify(result)

@app.route('/getusers/<user_full_name>')
def get_users_list(user_full_name):
    where = ( User.last_name.like(user_full_name+'%')  or
             User.first_name.like(user_full_name+'%') 
            )
    user_list = db.session.query(User).filter(where).all()
    
    if len(user_list)>0:
        result = users_schema.dump(user_list)
        return jsonify(result) 
    else:   
        return {},404


@app.route('/getuser')
def get_users_by_query_id():

    try:
        p_user_id = request.args.get('id')
    except:
        p_user_id = ''


    try:
        p_user_name = request.args.get('username')
    except:
        p_user_name=''

    try:
        p_first_name = request.args['first_name']
    except:
        p_first_name=''


    where = (
             (not p_user_id or User.id==p_user_id) and 
             (not p_user_name or User.user_name==p_user_name) and
             (not p_first_name or User.first_name==p_first_name.capitalize())
             )
    print(p_user_id,p_user_name,where)

    user_list = db.session.query(User).filter(where).all()
    
    if len(user_list)>0:
        result = users_schema.dump(user_list)
        return jsonify(result) 
    else:   
        return {},404

@app.route('/edituser',methods=['PUT'])
def edit_user():
    try:
        body = request.get_json()

        user_obj = {
            "id":body['id'],
            "user_name":body['username'],
            "password" :body['password'],
            "first_name":body['firstName'],
            "last_name":body['lastName'],
            "user_type":body['userType']
        }

        # new_user = User(user_obj['user_name'],user_obj['password'],user_obj['first_name'],user_obj['last_name'],user_obj['user_type'])        
        found_user = User.query.get(user_obj['id'])
        # print(found_user.password)
        found_user.password=user_obj['password']
        db.session.commit()

        return user_obj,200

    except Exception as ex:
        print(ex)
        codes = 100

        return {"message":str(ex)},417


@app.route('/change-pass',methods=['PUT'])
def change_pass():
    try:
        body = request.get_json()

        user_obj = {
            "user_name":body['username'],
            "password" :body['password']
        }

        found_user = User.query.filter_by(user_name=user_obj['user_name']).first()
        print(found_user)
        found_user.password=user_obj['password']
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
