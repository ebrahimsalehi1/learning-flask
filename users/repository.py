from flask import json

def read_data():
    with open("./sampledata/db.json") as db:
        data = json.load(db)

    return data

def create_data():
    pass

def update_data():
    pass

def delete_data():
    pass
