
from init import db

class Gender(db.Model):
    id=db.Column(db.Integer,primary_key=True,autoincrement=True)
    title = db.Column(db.String,unique=True)
    users = db.relationship('User',backref='gender',lazy=True)

    def __init__(self,title):
        self.title=title
