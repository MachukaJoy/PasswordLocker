#!/usr/bin/env python

from passlocker import User
from passlocker import Credentials


def create_user(fname, sname, loginkey):
  '''
  Function to create a new user
  '''
  new_user = User(fname, sname, loginkey)
  return new_user

def save_user(user):
  '''
  Function to save user
  '''
  user.save_user()


def save_credentials(credentials):
  '''
  Function to save credentials
  '''
  credentials.save_credentials()


def del_credentials(credentials):
  '''
  Function to delete a credential
  '''
  credentials.delete_credentials()


def find_credentials(account):
  '''
  Function that finds an account by number and returns the account
  '''
  return Credentials.find_by_account(account)


def display_credentials():
  '''
  Function that returns all the saved credentials
  '''
  return Credentials.display_credentials()


# create main function
def main() :
  print("Hi!This is Password Manager.What is your name")
  user_name = input()

  print(f"Great ! What would you like to do { user_name }?")
  print('\n')

  while True: 
      print("Lets create an account or Login to proceed or exit. Use IN to login, CA to Create Account or EXIT to exit application ")
      # print("lets proceed use IN or CA")
      user_input =input()
      if user_input =="CA":
          print("Proceed to create your password Locker Account")
          print("--"*20)
          print("Enter your First Name")
          fname = input()
          print("Enter your Last Name")
          sname = input()
          print("Enter your login key")
          loginkey = input()
    
          #Saving the user created credentials
          save_user(create_user(fname, sname, loginkey))
          print("Your password-locker account created successfully...please proceed to login")
          print("--" *20)
          print(f"FullNames -> {fname}{sname} \n User Name -> {user_name} \nloginkey/loginkey -> {loginkey}")
          print("|     ___   ____      _   ")
          print("|    |   | |  __  |  | \  |")
          print("|___ |___| |___|  |  |  \_|")
          print("Please provide your user Name")
          usernameaccount = input()
          print("Provide your loginkey")
          loginkey = input()
          if usernameaccount == user_name and loginkey ==loginkey:
              print("Successfully Logged In..welcome.......")
              print("**"*10)
          pass


if __name__ == '__main__':

        main()