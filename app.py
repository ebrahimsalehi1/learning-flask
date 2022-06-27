
from distutils.log import debug
from flask import Flask
from flask import render_template
from flask import url_for,request,jsonify,json

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

@app.route("/isemployee/<employee_id>")
def is_employe():
    return render_template('index.html')

@app.route('/login',methods=['GET','POST'])
def login():
    if request.method=='GET':
        return render_template('login.html')
    else:
        json_file= open('db.json')
        data=json.load(json_file)
        json_file.close()
        print(data['users'])

        return jsonify(data['users'])


@app.route('/checkUser/<string:userId>',methods=['POST'])
def checkUser(userId):
    print(request.json["message"])
    return "checkUser"


with app.test_request_context():
    # print(url_for('isemployee'))
    # print(url_for('isemployee',employee_id='100'))
    print(url_for('index'))

if __name__=="__main__":
    app.run(debug=True)
    