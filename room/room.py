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
        


     
