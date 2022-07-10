import numpy as np

arr = np.array([
    {
      "userId": 100,
      "username": "ebrahim2000",
      "password": "1234",
      "firstName": "ebrahim",
      "lastName": "salehi",
      "userType": "teacher"
    },
    {
      "userId": 101,
      "username": "mahsa4321",
      "password": "4321",
      "firstName": "mahsa",
      "lastName": "hakamiha",
      "userType": "student"
    }
    ,
    {
      "userId": 102,
      "username": "mahsa4321",
      "password": "4321",
      "firstName": "esmail",
      "lastName": "salehi",
      "userType": "student"
    }
  ])

indexes = [i for i in range(len(arr)) if arr[i]["userType"]=='teacher']

# for i in indexes:
#     print(arr[i])

def next_id():
    max=0
    for item in arr:
        if item["userId"]>max:
            max=item["userId"]

    return max

def create_record(userName,firstName,lastName,password="123",userType="student"):
    return {
      "userId": next_id(),
      "username": userName,
      "password": password,
      "firstName": firstName,
      "lastName": lastName,
      "userType": userType
    }

def delete_user(userId):
    print(arr)

# print(create_record(userName="admin",firstName="javad",lastName="salehi"))

delete_user('111')
