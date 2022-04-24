#!/usr/bin/env python3.9
from cgi import print_directory
from hashlib import new
from random import  randint 
from password import Password

def create__password(accname,username,phone,password):
    new_password =Password(accname,username,phone,password)
    return new_password


def save_password(password):
    password.save_password()

def generate_random_password(abcdghjkBNHGFUIGY123490):
    random_password =Password(abcdghjkBNHGFUIGY123490)
    return random_password


def del_password(password):
    password.delete_password() 

def  check_existing_passwords(username):
     return Password.password_exists(username)  

def display_password():
    return Password.display_passwords() 



# generating a random pasword
print("generate a random password for your account")
def genP(ln)  : 
    print("generate a random password")
    login ="abcdfhjkioersHJOOIDIWOWW1234567!@#$%&"
    pasw1 = ""
    for i in range(ln):
        pasw1+=login[randint(0,35)]
    return pasw1
print(genP(10))        
print(genP(10))    
# print(len(genP))      





    


def main():


    print("Habari! Welcome to your password list. What is your name")
    user_name = input()
    print(f"Hello{user_name}.what would you like to do")

    print('.\n')





    while True:

        print ("use this short codes: cp- create a new password,dp-display passwords,cr- search for random password,cx- exit the password")

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


            # save_password(generate_random_password)(abcdghjkBNHGFUIGY123490)
            # print('.\n')
            # print(f"password{abcdghjkBNHGFUIGY123490}")


            save_password(create__password(accname,username,phone,password)) 
            print('.\n')
            print(f"username{username}password{password}created")  
            print('.\n')







        elif short_code == "dp" :   
            if display_password() :
                print("Here is a list of all passwords")
                print('\n')
                for password in display_password():
                    print(f"{password.account_name}){password.username}....{password.account_password}")
                    print('.\n')

            else:
                print('/n')
                print("you dont seem to have any login details")
                print('.\n')


            

        elif short_code == "cr" :
            print("search for random password")

            search_username= input()
            if check_existing_passwords(search_username) :

                print(f"{search_username.phone}{search_username.account_name}")


                print('-'*20)   
                print(f"phone number......{search_username.phone}")
                print(f"Email address....{search_username.accout_name}")


            else :
                print("That password does not exist")













            




    














if __name__ == '__main__':
    main()

