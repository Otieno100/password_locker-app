#!/usr/bin/env python3.9
from random import random
from password import Password

def create__password(accname,username,phone,password):
    new_password =Password(accname,username,phone,password)
    return new_password


def save_password(password):
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
    user_name = input()
    print(f"Hello{user_name}.what would you like to do")

    print('.\n')


    while True:

        print ("use this short codes: cp- create a new password,dp-display passwords,cr- create random password,cx- exit the password")

        short_code = input().lower()
        if short_code == "cp":
            print("new password")
            print("-"*5)
             
            print("acount name......")
            accname =input()

            print("add username.........")
            username =input()


            print("phone_number ......")
            phone = input()

            print("password.......")
            password = input()

            


            save_password(create__password(accname,username,phone,password)) 
            print('.\n')
            print(f"username{username}password{password}created")  
            print('.\n')




    














if __name__ == '__main__':
    main()

