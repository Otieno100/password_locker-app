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
        

    def test_generate_random_password(pas) :

        """
        test case to define the instance of generating a random password

        """
        pas.new_password.save_password(pas)
        pas.assertEqual(len(Password.password_list),2)
        



if __name__=="__main__":
    unittest.main()
