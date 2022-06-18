
from distutils.log import debug
from flask import Flask

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

if __name__=="__main__":
    app.run(debug=True)
    