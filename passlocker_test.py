import unittest # Importing the unittest module
from passlocker import User #Importing the User class
from passlocker import Credentials #imports Credentials class

class TestUser(unittest.TestCase):
    """
    Test class that defines test cases for the user class behaviours.
    Args:
        unittest.TestCase: TestCase class that helps in creating test cases
    """

    def setUp(self):
        '''
        Set up method to run before each test cases.
        '''
        self.new_user = User("Joy","Machuka","0001") # create user object
        self.new_credentials = Credentials("instagram","msmachuka","Fr1d@y") #create credentials object

    def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''

        self.assertEqual(self.new_user.fname,"Joy")
        self.assertEqual(self.new_user.sname,"Machuka")
        self.assertEqual(self.new_user.loginkey,"0001")


        self.assertEqual(self.new_credentials.account,"instagram")
        self.assertEqual(self.new_credentials.username,"msmachuka")
        self.assertEqual(self.new_credentials.password,"Fr1d@y") 

if __name__ == '__main__':
    unittest.main()