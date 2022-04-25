#!/usr/bin/env python3.8

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
