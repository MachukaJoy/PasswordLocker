#!/usr/bin/env python

from passlocker import User
from passlocker import Credentials


def create_user(fname, sname, loginkey):
  '''
  Function to create a new user
  '''
  new_user = User(fname, sname, loginkey)
  return new_user


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
  my_name = input()

  print(f"Great ! What would you like to do { my_name }?")
  print('\n')

  while True:
    print("Choose a short code : ca - create a new credential, dc - display credentials, fc -find credential, ex -exit credential list ")

    short_code = input().lower()


if __name__ == '__main__':

        main()