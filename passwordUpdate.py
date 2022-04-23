# from cgi import test
import unittest

from password import Password
class testclass (unittest.TestCase) :


    def setUp(pas):

     pas.new_password = Password("instagram", "John", "077777777","brian102@")

    def test_init (pas):
        pas.assertEqual(pas.new_password.account_name,"instagram")
        pas.assertEqual(pas.new_password.username,"John")
        pas.assertEqual(pas.new_password.phone_number ,"077777777")

        pas.assertEqual(pas.new_password.account_password,"brian102@")


    def test_save_password(pas) :

        """
        test case that defines the instance of saving the password
        """
        pas.new_password.save_password()
        pas.assertEqual(len(Password.password_list),1)

    def tearDown(pas) :
        Password.password_list =[]
        

    def test_generate_random_password(pas) :

        """
        test case to define the instance of generating a random password

        """
        pas.new_password.save_password()
        test_password =Password("Test","user","abcdef023444!!@","passw@10.com")
        test_password.save_password()
        pas.assertEqual(len(Password.password_list),2)


    def test_delete_password(pas):
        """
        instance to delete our password
        """
        pas.new_password.save_password ()
        test_password = Password("instagram", "John", "077777777","brian102@")  
        test_password.save_password()
        pas.new_password.delete_password()
        pas.assertEqual(len(Password.password_list),1)


    def test_find_password_by_username(pas) :

        """
            this test checks if we can find a password using username

        """
        pas.new_password.save_password()
        test_password =Password("instagram", "John", "077777777","brian102@")
        test_password.save_password()
        found_password = Password.find_by_username("John")
        pas.assertEqual(found_password.username,test_password.username)


    def test_display_all_password(pas):

        '''
        method that returns list of all the saved items

        '''
        pas.assertEqual(Password.display_passwords(),Password.password_list)

        











if __name__=="__main__":
    unittest.main()
