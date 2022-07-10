
from flask import Flask
from flask import render_template,request,json,jsonify
 
app = Flask(__name__)

with open("db.json") as db:
    data = json.load(db)

@app.route("/")
@app.route("/home")
def index():
    return "Hello World !!!"

@app.route("/users",methods=["GET"])
def users():  
    return jsonify(data["users"])      

@app.route("/users",methods=["POST"])
def user_save():
    body = request.get_json()
    data["users"].append(body)
    return body

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


@app.route('/numpy')
def py():
    import numpy as np
    res = np.array([1,2,3])
    # res=np.array([1,2,3],ndmin=3)
    print(np.arange(9).reshape(1,10))
    return "using numpy is awesome"

if __name__=="__main__":
    app.run(debug=True)
    