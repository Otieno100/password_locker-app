

from random import randint
import pyperclip


class Password :
    """
    Class that generates new instances of contacts.
    """
  

    def __init__(pas, account_name, username, number, account_password):

      

        pas.account_name = account_name
        pas.username = username
        pas.phone_number = number
        pas.account_password = account_password

    password_list = []

    def save_password(pas):

        """
        save password method, saves password objects into password list

        """
        Password.password_list.append(pas)



    def delete_password(pas) :

        """
        this method deletes the saved contacts
        """
        Password.password_list.remove(pas)


    @classmethod
    def find_by_username(cls,username):
        '''
        the method takes in a username and return the password being searched

        '''

        for password in cls.password_list :
            if password.username == username :
                return password


    @classmethod
    def display_passwords(cls):
        """
        method that returns all the saved credentials
        """
        return cls.password_list


    def random_password (cls):

        ran = "bcadreskahajajaDGJKJN09765347865!!!@"
        pasw = ""
        for i in range(cls) :
            pasw +=ran[(randint(0,10))]
        return(pasw)

    @classmethod
    def copy_username(cls,username) :

        """
        test method to copy details on clip-board
        """
        password_found = Password.find_by_username(username)
        pyperclip.copy(password_found.username)

