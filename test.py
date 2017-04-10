from room import LivingSpace, Office
import unittest
class TestDojoProject(unittest.TestCase):
    def setUp(self):
        self.Office=Office("blue")
        self.LivingSpace=LivingSpace("simba")
        
    def test_space(self):
            room_type = "Office"
            self.assertEqual(self.Office.maxspace, 6)

            room_type = "LivingSpace"
            self.assertEqual(self.LivingSpace.maxspace, 4)
    def test_Room_type(self):
            self.assertEqual(self.Office.room_type, "Office"
                             ,msg ="Room can either be Office or LivingSpace")
            self.assertEqual(self.LivingSpace.room_type, "LivingSpace"
                             ,msg ="Room can either be Office or LivingSpace")




if __name__ == '__main__':
    unittest.main(verbosity=2)
