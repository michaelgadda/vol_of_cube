import unittest 
from vol_of_cube import cube



class TestCubeVolume(unittest.TestCase):
    
    def test_corrrectness(self):
    	self.assertEqual(cube.vol_of_cube(5), 125)
    	self.assertEqual(cube.vol_of_cube(3), 27)
    	self.assertEqual(cube.vol_of_cube(0.5), 0.125)
    	self.assertEqual(cube.vol_of_cube(555), 170953875)
    
    def test_type(self):
    	self.assertEqual(cube.vol_of_cube("QQ"), "The length of your edge can not be a string")
    	self.assertEqual(cube.vol_of_cube(True), "The length of your edge can not be a boolean value")
    	self.assertNotEqual(cube.vol_of_cube(5), "The length of your edge can not be a string")
    	self.assertNotEqual(cube.vol_of_cube(5), "The length of your edge can not be a boolean value")

    def test_negative(self): 
    	self.assertEqual(cube.vol_of_cube(-5), "The length needs to be greater than 0")
    	self.assertNotEqual(cube.vol_of_cube(5), "The length needs to be greater than 0")
    	self.assertEqual(cube.vol_of_cube(-555), "The length needs to be greater than 0")

if __name__ == '__main__': 
	unittest.main()


#COMMAND LINE INPUT: python -m unittest -v vol_of_cube_test.py