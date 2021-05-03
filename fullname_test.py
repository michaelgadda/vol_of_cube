import unittest 
from fullname_calculator import fullname 



class TestFullName(unittest.TestCase):
    
    def test_corrrectness(self):
    	self.assertEqual(fullname.first_plus_lastname("Michael", "Gadda"),"Michael Gadda")
    	self.assertEqual(fullname.first_plus_lastname("John", "Smith"), "Johnny Smith")
    	self.assertEqual(fullname.first_plus_lastname("Alexander", "Balish"), "Alexander Balish")
   
    def test_type(self):
    	self.assertEqual(fullname.first_plus_lastname("M1ke" , "Ga66a"), "Your first contains a non alphabetic character, please remove it and try again!")
    	self.assertEqual(fullname.first_plus_lastname("John", "--Sm1th~~"), "Your last name contains a non alphabetic character, please remove it and try again!")
    	self.assertNotEqual(fullname.first_plus_lastname("Mike", "Gadda"), "Your first contains a non alphabetic character, please remove it and try again!")
    	self.assertNotEqual(fullname.first_plus_lastname("Mike", "Gadda"), "The length of your edge can not be a boolean value")

    def test_null(self): 
    	self.assertEqual(fullname.first_plus_lastname("","Jones"), "You have forgot to enter your first name, please do so and try again")
    	self.assertEqual(fullname.first_plus_lastname("Bob", ""), "You have forgot to enter your last name, please do so and try again")
    	self.assertNotEqual(fullname.first_plus_lastname("Michael", "Gadda"), "You have forgot to enter your first name, please do so and try again")

if __name__ == '__main__': 
	unittest.main()
