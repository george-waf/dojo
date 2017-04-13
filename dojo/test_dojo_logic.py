import unittest
from dojo_logic import DojoLogic


class TestDojo(unittest.TestCase):

    def setUp(self):
        self.MyDojo = DojoLogic()

    def test_officespace_creation(self):      
        self.MyDojo.create_room("Office", "green")

    def test_livingspace_creation(self):        
        self.MyDojo.create_room("Livingspace", "simba")

    def test_adding_fellow(self):        
        self.MyDojo.add_person("george", "wafula","Fellow", "n")

    def test_adding_staff(self):      
        self.MyDojo.add_person("george", "wafula", "Staff","n")

    

        
if __name__ == '__main__':
        unittest.main(verbosity=2) 
