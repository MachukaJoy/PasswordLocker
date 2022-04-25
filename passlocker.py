class User:
  user_list = [] # Empty user list

  def __init__(self,username,password):

    """
    __init__ method that helps us define properties for our objects.
    Args:
        username : New user username.
        password : New user password.
    """

    self.username = username
    self.password = password 

  pass

#Credentials class
class Credentials :
  """
  Class that creates new instances of credentials
  """
  credentials_list = [] # Empty credentials list

  def __init__(self,account,username,password):

    """
    __init__ method that helps us define properties for our objects.
    Args:
      username : New user username.
      password : New user password.
    """
    self.account = account
    self.username = username
    self.password = password
