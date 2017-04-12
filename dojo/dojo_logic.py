import os
from person.person import Fellow, Staff
from room.room import Office, LivingSpace

class DojoLogic(object):

	def __init__(self):
                self.office_directory = []
                self.livingspace_directory = []
                self.fellows_directory = []
                self.staff_directory = []
		
		

	def create_room(self, name, room_type):
	    if name in (office.name for office in self.office_directory):
                    print ('office {} already exists'.format(name))
            else:
		if room_type == "office":
                         	
			new_office = Office(name)
			self.office_directory.append(new_office)
			print ('An Office called {} has been successfully created'.format(name))
			return self.office_directory			
            if name in (livingspace.name for livingspace in self.livingspace_directory):
                    print ('Livingspace {} already exists'.format(name))
            else:
		if room_type == "livingspace":
								
			new_livingspace = LivingSpace(name)
			self.livingspace_directory.append(new_livingspace)
			print ('Living Space {} has been  created'.format(name))
			print(self.livingspace_directory)	
		
		
					
	def add_person(self, first_name, second_name, position, wants_accomodation="n"):
		
		if position == "staff":
			
			new_staff = Staff(first_name, second_name)
			self.staff_directory.append(new_staff)
			print ('Staff {} has been successfully added'.format(first_name))
							
		elif position == "fellow":
			
			new_fellow = Fellow(first_name, wants_accomodation)
			self.fellows_directory.append(new_fellow)
			print ("Fellow {} has been successfully added\n" .format(first_name))
									
			try:
				if new_fellow.wants_accomodation == "y":
					print ('added to accomodation')
			except AttributeError:
				return
			

		
	
