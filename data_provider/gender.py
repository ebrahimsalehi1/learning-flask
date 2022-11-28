from init import db
from model.user import User
from model.gender import Gender
from model.user_type import Usertype
from sqlalchemy import func

def provide_gender_data():
    try:
        db.session.query(Gender).delete()
        db.session.add(Gender(title='Female'))
        db.session.add(Gender(title='Male'))
        db.session.commit()
    except Exception as ex:
        print(ex)
        db.session.rollback()
        