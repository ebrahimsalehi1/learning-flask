from init import db
from model.user import User

def add_new_user(user_obj):
    new_user = User(user_obj['user_name'],user_obj['password'],user_obj['first_name'],user_obj['last_name'],user_obj['user_type'])
    print(new_user.id)
    db.session.add(new_user)
    db.session.commit()


def get_users():
    all_users = User.query.all()
    str_result ='['
    i=0
    for user in all_users:
        str_result = str_result+str(user.get_json())
        if i<len(all_users)-1:
            str_result=str_result+","

        i=i+1

    str_result=str_result+']'    