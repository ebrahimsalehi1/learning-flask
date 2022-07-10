from flask import redirect,url_for,Blueprint,json,jsonify,request
import numpy 

users = Blueprint("users",__name__,static_folder="static",template_folder="templates")

print("hello ")

with open('db.json') as db:
    data = json.load(db)

@users.route("/",methods=["GET"])
def user():
    return jsonify(data["users"])

@users.route("/",methods=["POST"])
def use_save():
    body = request.get_json()
    data["users"].append(body)
    return body

@users.route("/",methods=["PUT"])
def use_update():
    body = request.get_json()
    # index = i for i in range(data["users"]) if data["users"]["userId"]==body.userId
    # data["users"]
    return body

@users.route("/admin")
def admin():
    return "Hello ADMIN"
    # return redirect(url_for("user",name="Admin!"))
