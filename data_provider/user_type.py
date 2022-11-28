from init import db
from model.user import User
from model.gender import Gender
from model.user_type import Usertype
from sqlalchemy import func

def provide_user_type_data():
    try:
        db.session.query(Usertype).delete()
        db.session.add(Usertype(title='Teacher'))
        db.session.add(Usertype(title='Student'))
        db.session.add(Usertype(title='General'))
        db.session.add(Usertype(title='Admin'))
        db.session.add(Usertype(title='Employee'))

        db.session.commit()
    except Exception as ex:
        print(ex)
        db.session.rollback()
        