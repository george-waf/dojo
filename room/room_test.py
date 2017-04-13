import unittest
from room import Office, LivingSpace
class TestCreateRoom(unittest.TestCase):
		
	def setUp(self):
		self.office_space = Office("Red")
		self.living_space = LivingSpace("Simba")
	
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

     
