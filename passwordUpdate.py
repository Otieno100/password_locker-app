# from cgi import test
import unittest

from password import Password
class testclass (unittest.TestCase) :


    def setUp(pas):

     pas.new_password = Password("Brian", "otieno", "077777777","b@gmail.com")

    def test_init (pas):
        pas.assertEqual(pas.new_password.first_name,"Brian")
        pas.assertEqual(pas.new_password.last_name,"otieno")
        pas.assertEqual(pas.new_password.phone_number,"077777777")
        pas.assertEqual(pas.new_password.email,"b@gmail.com")
        





if __name__=="__main__":
    unittest.main()
