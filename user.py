#!/usr/bin/env python3.9
from random import random
from password import Password

def create__password(accname,username,phone,password):
    new_password =Password(accname,username,phone,password)
    return new_password


def save_passwords(password):
    password.save_password()

def generate_random_password(password):
    return Password.random_password(password)


def del_password(password):
    password.delete_password() 

def  check_existing_password(username):
     return Password.password_exists(username)  

def display_password():
    return Password.display_passwords() 


def main():
    print("Habari! Welcome to your password list. What is your name")















if __name__ == '__main__':
    main()

