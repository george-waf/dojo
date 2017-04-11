class Room(object):
    def __init__(self, name):
        self.name = name
	   
class Office(Room):
    def __init__(self, name):
        self.name = name
        self.room_type = 'office'
        self.max_space = 6
        
class LivingSpace(Room):
    def __init__(self, name):
        self.name = name
        self.room_type = 'livingspace'
        self.max_space = 4
        
import unittest
class TestCreateRoom(unittest.TestCase):
		
	def setUp(self):
		self.office_space = Office("R")
		self.living_space = LivingSpace("Emerald")
	
	def test_officespace_size(self):
		self.assertEqual(self.office_space.max_space, 6)
			
	def test_officespace_type(self):
		self.assertEqual(self.office_space.room_type, "office")
			
	def test_livingspace_size(self):
		self.assertEqual(self.living_space.max_space, 4) 
			
	def test_livingspace_type(self):
		self.assertEqual(self.living_space.room_type, "livingspace")
				

if __name__ == '__main__':
    unittest.main(verbosity=2)  

     
