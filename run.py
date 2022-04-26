#!/usr/bin/env python

from passlocker import User
from passlocker import Credentials
import random
import string


def create_user(fname, sname, loginkey):
  '''
  Function to create a new user
  '''
  new_user = User(fname, sname, loginkey)
  return new_user
def create_credentials(account,username,password):
        """
        Function to create new credentials
        """
        new_credentials = Credentials(account,username,password)
        return new_credentials        

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
      login = input()
      if usernameaccount == user_name and login ==loginkey:
        print("Successfully Logged In..welcome.......")
        print("**"*10)

      pass
      while True:
        print("Use the following initials to create, view and delete accounts")
        print("CRE to create new credential account")
        print("SAVE to save existing credentials account details")
        print("VIEW to view credential account")
        print("DEL to delete credential account")
        print("EXIT to exit password locker")

        user_input = input()
        if user_input == "CRE":
          print("Now creating a new credentials account details...")
          print("*-")
          
          print("Enter the account type e.g twitter , instagram...")
          account= input()
          
          print("Enter your username...")
          username = input()

          print("Can we generate a password for you ..Y/N Y(yes) and N(No)")
          password = input()

          if password == "Y":
            print("provide the length of your passcode e.g 10")
            password_length = int(input())
            passwordcharacters = string.ascii_letters +string.digits
            password = "".join(random.choice(passwordcharacters )for i in range(password_length))
          elif password == "N":
              print("Please provide your security passcode ....")
              password = input()
          else:
              print("check your input once more")
        
          


if __name__ == '__main__':

        main()