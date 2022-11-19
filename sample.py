
from flask import Flask
from flask import render_template,request,json,jsonify
from users.controller import users
from  flask_mysqldb import MySQL

app = Flask(__name__)
mysql = MySQL(app)

app.register_blueprint(users,url_prefix='/users')

@app.route("/")
@app.route("/home")
def index():
    return "Hello World !!!"


@app.route('/')
def index():
    cur = mysql.connect.cursor()
    # cur.execute('CREATE TABLE TABLE1(NUM INTEGER)')
    cur.execute('INSERT INTO TABLE1 VALUES(20)')
    cur.connection.commit()
    return "Done !!!!"


if __name__=="__main__":
    app.run(debug=True)
    