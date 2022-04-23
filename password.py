

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
