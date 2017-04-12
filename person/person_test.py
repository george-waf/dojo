import unittest
from person import Staff, Fellow
class TestPerson(unittest.TestCase):
	"""Test instance of Person added"""
	
	def setUp(self):
		self.fellow = Fellow('george')
		self.staff = Staff('tim','juma')

	def test_person_role_is_fellow(self):
		self.assertEqual(
			self.fellow.position, 'fellow')
			

	def test_person_role_is_staff(self):
		self.assertEqual(
			self.staff.position, 'staff')
			
	def test_staff_invalid_accomodation_option(self):
		self.assertEqual(
			self.staff.wants_accomodation,'n')
			
if __name__ == '__main__':
    unittest.main(verbosity=2)  
