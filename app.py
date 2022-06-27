
from distutils.log import debug
from flask import Flask
from flask import render_template,request
 

app = Flask(__name__)

@app.route("/")
def index():
    return "Hello World !!!"

@app.route("/employee")
def employee():
    employee = {
        "firstName":"ebrahim"
    }

    return employee

@app.route("/isemployee")
def is_employe():
    return render_template('index.html')

@app.route('/employeeList')    
def employeeList():
    from make_data import get_data
    return render_template('index.html',name='qwqw',empList= map(lambda i:i["salary"],get_data()))

@app.route('/user/<string:userName>/<int:password>')
def get_user(userName,password):
    return f"user: {userName} - {password}"

@app.route('/calculate/<string:operation>/<float:n1>/<float:n2>')
def calculate(operation,n1,n2):
    res=0
    if operation=='add':
        res=n1+n2
                
    return f"calc - {operation} - {res}"

@app.route('/calculate',methods=['POST'])
def calculate2():
    operation = request.args.get("operation")
    n1 = request.args.get("n1")
    n2 = request.args.get("n2")

    res=0
    if operation=='add':
        res=n1+n2

    print(request.args.get("operation"))
                
    return f"calc - {operation} - {res}"

@app.route('/login/<string:user>/<string:password>',methods=['GET','POST'])
def login(user,password):
    if request.method=='GET':
        return render_template('login.html')
    else:
        user = request.args.get("user")    
        password = request.args.get("password")    

        if user=='ebrahim' and password=='1234':
            return "OK"
        else:
            return "Cancel"


@app.route('/path/<path:sub_path>')
def get_path(sub_path):
    return f"path: {sub_path}"

if __name__=="__main__":
    app.run(debug=True)
    