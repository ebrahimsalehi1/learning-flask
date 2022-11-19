from flask import Flask,request,jsonify,render_template
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from sqlalchemy import func,case,desc,asc
import datetime as dt
from flask_migrate import Migrate
from dotenv import load_dotenv
import os

from init import app,db,ma,migrate
from model.user import User
import controller.general 
import controller.user


@app.route('/upload/<user_id>',methods=['GET','POST'])
def upload(user_id):
    found_user = db.session.query(User).filter(User.id==user_id).first()
    if not found_user:
        return {"result":"Not Found"}

    if request.method=='GET':
        return render_template('index.html')

    elif request.method=='POST':
        uploaded_file = request.files['filename']
        found_user.image = uploaded_file.read()
        db.session.commit()
        return "POST is done"    


if __name__=='__main__':
    app.run(debug=True)
