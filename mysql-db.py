
from flask import Flask
from flask import render_template,request,json,jsonify
# from users.controller import users
from  flask_mysqldb import MySQL
from dotenv import load_dotenv
import os

app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:root@localhost/restaurant'

app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('SQLALCHEMY_DATABASE_URI')
app.config['MYSQL_USER']=os.getenv('MYSQL_USERNAME')
app.config['MYSQL_PASSWORD']=os.getenv('MYSQL_PASSWORD')
app.config['MYSQL_HOST']=os.getenv('MYSQL_SERVER')
app.config['MYSQL_DB']=os.getenv('MYSQL_DB_NAME')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

mysql = MySQL(app)
# mysql://localhost:3306/restaurant

# app.register_blueprint(users,url_prefix='/users')

# @app.route("/test23")
# @app.route("/home23")
# def index():
#     return "Hello World !!!"


@app.route('/test23')
def index():
    cur = mysql.connect.cursor()
    # cur.execute('CREATE TABLE TABLE1(NUM INTEGER)')
    # cur.execute('INSERT INTO TABLE1 VALUES(20)')
    cur.execute('create database learning_flask')
    cur.connection.commit()
    return "Done !!!!"


if __name__=="__main__":
    app.run(debug=True)
    