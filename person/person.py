class Person(object):
	
	def __init__(self,first_name,second_name):
		self.name = first_name
		


class Staff(Person):
	
	def __init__(self, first_name,second_name):
		super(Staff, self).__init__(first_name,second_name)
		self.position = "staff"
		self.wants_accomodation = "n"
		

class Fellow(Person):
	
	def __init__(self, first_name,second_name, wants_accomodation="n"):
		super(Fellow, self).__init__(first_name,second_name)
		self.position = "fellow"
		self.wants_accomodation = wants_accomodation
