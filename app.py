
from flask import Flask
from  flask_mysqldb import MySQL
app = Flask(__name__)
from dotenv import load_dotenv
import os

app.config['MYSQL_USER']=os.getenv('MYSQL_USERNAME')
app.config['MYSQL_PASSWORD']=os.getenv('MYSQL_PASSWORD')
app.config['MYSQL_HOST']=os.getenv('MYSQL_SERVER')
app.config['MYSQL_DB']=os.getenv('MYSQL_DB_NAME')
# app.config['MYSQL_CURSORCLASS']='DictCursor'


mysql = MySQL(app)


@app.route('/')
def index():
    cur = mysql.connect.cursor()
    # cur.execute('CREATE TABLE TABLE1(NUM INTEGER)')
    cur.execute('INSERT INTO TABLE1 VALUES(20)')
    cur.connection.commit()
    return "Done !!!!"

if __name__=='__main__':
    app.run(debug=True)
