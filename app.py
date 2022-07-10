
from re import I
from flask import Flask
from flask import render_template,request,json,jsonify
from user_repository import read_data
from user_services import read_service,create_service,delete_service
app = Flask(__name__)

data = read_data()

@app.route("/")
@app.route("/home")
def index():
    return "Hello World !!!"

@app.route("/users",methods=["GET"])
def users():  
    return read_service(data["users"])

@app.route("/users",methods=["POST"])
def user_save():
    body = request.get_json()
    return create_service(users_list=data["users"],user=body)

@app.route("/users",methods=["PUT"])
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

@app.route("/users/<string:userId>",methods=["GET"])
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

@app.route('/users/<int:user_id>',methods=["DELETE"])
def delete_user(user_id):
    return delete_service(users_list=data["users"],user_id=user_id)

if __name__=="__main__":
    app.run(debug=True)
    