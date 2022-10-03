from flask import Flask,request,Blueprint,jsonify
from users.repository import read_data
from users.service import read_service,create_service,delete_service
from users.validate import check_validation

users = Blueprint("users",__name__)

data = read_data()

@users.route("/",methods=["GET"])
def get_users():  
    return read_service(data["users"])

@users.route("/save",methods=["POST"])
def user_save():
    body = request.get_json()

    if not check_validation(body):
        return {"message":"userType is not valid"},417
    else:    
        return create_service(users_list=data["users"],user=body)

@users.route("/",methods=["PUT"])
def user_update():
    body = request.get_json()
    arr = data["users"]
    for i in range(len(arr)):
        if arr[i]["userId"]==body["userId"]:
            index=i
            break

    data["users"][index]=body
    print(index)
    print(data["users"][index])
    return body

@users.route("/<string:userId>",methods=["GET"])
def get_by_id(userId):
    arr = data["users"]
    userFound = None
    for item in arr:
        if str(item["userId"])==str(userId):
            print(item["userId"])
            userFound = item
            break

    if userFound:
        return userFound
    else:
        return jsonify(None)

@users.route('/<int:user_id>',methods=["DELETE"])
def delete_user(user_id):
    return delete_service(users_list=data["users"],user_id=user_id)

