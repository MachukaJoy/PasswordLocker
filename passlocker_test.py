import unittest # Importing the unittest module
from passlocker import User #Importing the User class

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
        self.new_user = User("Machuka","PassW@hala") # create user object

    def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''

        self.assertEqual(self.new_user.username,"Machuka")
        self.assertEqual(self.new_user.password,"PassW@hala")

if __name__ == '__main__':
    unittest.main()