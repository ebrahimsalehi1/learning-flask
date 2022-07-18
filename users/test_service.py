import unittest
from service import read_service_base

users_list = [
    {
      "userId": 1,
      "username": "werew",
      "password": "1234",
      "firstName": "zahra",
      "lastName": "ahmadi",
      "userType": "driver"
    }
]

class TestService(unittest.TestCase):
    def test_read_user_id(self):
        result = read_service_base(users_list)
        print(result)
        self.assertEqual(result[0]['userId'],1)

    def test_read_first_name(self):
        result = read_service_base(users_list)
        print(result)
        self.assertEqual(result[0]['firstName'],'zahra090')


if __name__=='__main__':
    unittest.main()
    
