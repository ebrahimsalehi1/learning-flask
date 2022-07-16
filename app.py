
from flask import Flask
from flask import render_template,request,json,jsonify
from users.controller import users

app = Flask(__name__)
app.register_blueprint(users,url_prefix='/users')

@app.route("/")
@app.route("/home")
def index():
    return "Hello World !!!"

if __name__=="__main__":
    app.run(debug=True)
    