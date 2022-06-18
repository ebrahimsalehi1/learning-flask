
from distutils.log import debug
from flask import Flask
from flask import render_template

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

if __name__=="__main__":
    app.run(debug=True)
    