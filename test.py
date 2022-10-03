
users_list=[
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
  ]

# print(range(len(users_list)))
indexes = [i for i in users_list if i["userId"]==100 ]
print(indexes)