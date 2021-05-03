import unittest 
from average_of_list import list_



class TestAverageOfList(unittest.TestCase):
	
	list1 = [1,2,3,4,5,6]
	list2 = []
	list3 = [0]
	list4 = [10000, -1., .234, .5678, 12345]
	list5 = [123, 1, 2, 3, "hey"]
	list6 = [123, 3, True, False]   

	def test_corrrectness(self):
		self.assertEqual(list_.average_of_list(self.list1), 3.5)
		self.assertEqual(list_.average_of_list(self.list4), 4468.96036)
		self.assertEqual(list_.average_of_list(self.list3), 0)
	def test_type(self):
		self.assertEqual(list_.average_of_list(self.list5),"Please enter a list of ONLY numbers!")
		self.assertEqual(list_.average_of_list(self.list6), "Please enter a list of ONLY numbers!")
		self.assertNotEqual(list_.average_of_list(self.list1), "Please enter a list of ONLY numbers!")
		self.assertNotEqual(list_.average_of_list(self.list3), "Please enter a list of ONLY numbers!")
	def test_zero(self): 
		self.assertEqual(list_.average_of_list(self.list2), "Please enter more than 0 elements")
		self.assertNotEqual(list_.average_of_list(self.list3), "Please enter more than 0 elements")
    	
if __name__ == '__main__': 
	unittest.main()