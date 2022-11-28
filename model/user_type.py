from sqlalchemy import func,case,desc,asc
from app2 import db

class Usertype(db.Model):
    id=db.Column(db.Integer,primary_key=True,autoincrement=True)
    title = db.Column(db.String,unique=True)
    users = db.relationship('User',backref='usertype',lazy=True)

    def __init__(self,title):
        self.title=title
        