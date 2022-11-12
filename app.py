
from flask import Flask
from  flask_mysqldb import MySQL
app = Flask(__name__)

app.config['MYSQL_USER']='sql7564630'
app.config['MYSQL_PASSWORD']='niEecw6hk1'
app.config['MYSQL_HOST']='sql7.freemysqlhosting.net'
app.config['MYSQL_DB']='sql7564630'
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
