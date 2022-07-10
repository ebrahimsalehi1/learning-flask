from flask import jsonify

def read_service(users_list):
    return jsonify(users_list)      

def create_service(users_list,user):
    users_list.append(user)
    return jsonify(user)


def update_service():
    pass

def delete_service(users_list,user_id):
    indexes = [i for i in range(len(users_list)) if users_list[i]["userId"]==user_id]
    result=None

    for index in indexes:
        result=users_list[index]
        users_list.pop(index)

    return jsonify(result)
