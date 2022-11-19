
from flask import request,jsonify
from init import app,users_schema,user_schema,db
from model.user import User
from service.user import add_new_user,get_users

@app.route('/test')
def test():
    return "TEST"

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

        add_new_user(user_obj)

        return user_obj,200

    except Exception as ex:
        print(ex)
        codes = 100

        return {"message":str(ex)},417

@app.route('/getusers')
def get_users():
    return jsonify(get_users())


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


    try:
        page = int(request.args['page'])
    except:
        page=''

    try:
        size = int(request.args['size'])
    except:
        size=''

    # print(page,size)
    try:
        p_birth_date = request.args['birth_date'] #dt.datetime.strptime(str(request.args['birth_date']), "%Y-%m-%d").date() 
        p_birth_year = p_birth_date[0:4]
        p_birth_month = p_birth_date[5:7]
    except:
        p_birth_date=''
        p_birth_year=''
        p_birth_month=''

    # func.extract('year',User.birth_date)==p_birth_year and
    where = (
             (not p_user_id or User.id==p_user_id) and 
             (not p_user_name or User.user_name==p_user_name) and
             (not p_first_name or func.upper(User.first_name)==p_first_name.upper()) and
             (not p_birth_date or User.birth_month==p_birth_month)
             )
    
    user_list = db.session. \
                    query(User.user_name,User.full_name,User.gender_percent,User.birth_month).\
                    filter(where).\
                        order_by(asc("gender_id"),desc("first_name"))\
                            .offset(page*size)\
                            .limit(size)\
                            .all()
    
    # user_count = len(db.session.query(User).all())

    user_count_result= db.session.query(func.count(User.id)).first()
    user_count=user_count_result[0] if len(user_count_result)>0 else 0
    # print(user_count)

    if len(user_list)>0:
        result = users_schema.dump(user_list)
        return jsonify({'totalElements':user_count,'elements':result}) 
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


@app.route('/user/image/<user_id>')  
def show_user_image(user_id):
    found_user = db.session.query(User).filter(User.id==user_id).first()
    if not found_user:
        return {"result":"Not Found"}     

    return found_user.image