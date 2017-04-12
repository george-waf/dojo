class Room(object):
	
	def __init__(self, name):
		self.name = name
		
class Office(Room):
	
	def __init__(self, name):
		super(Office, self).__init__(name)
		self.room_type = "office"
		self.capacity = 6	
		
class LivingSpace(Room):
	
	def __init__(self, name):
		super(LivingSpace, self).__init__(name)
		self.room_type = "living space"
		self.capacity = 4

        


     
