import random
from person.person import Fellow, Staff
from room.room import OfficeSpace, LivingSpace

class DojoLogic(object):

    def __init__(self):
        self.office_directory = []
        self.livingspace_directory = []
        self.fellows_directory = []
        self.staff_directory = []
        

    def create_room(self, room_type, room_name):
        
        if room_type == "office":
            if room_name in [office.name for office in self.office_directory]:  
                print ('\n office {} already exists \n'.format(room_name))
            else:       
                                new_office = OfficeSpace(room_name)
                                self.office_directory.append(new_office)
                                print ('\n An Office called {} has been successfully created \n'
                                    .format(room_name))
                
        elif room_type == "livingspace":
            if room_name in [livingspace.name for livingspace in self.livingspace_directory]:
                print ('\n Living space {} already exists \n'.format(room_name))
            else:       
                                new_livingspace = LivingSpace(room_name)
                                self.livingspace_directory.append(new_livingspace)
                                print ( "\n A Living space called {} has been successfully created\n"
                                    .format(room_name))
                                
    def add_person(self, first_name, second_name, position, wants_accomodation="N"):
        if position == "staff":
            new_staff = Staff(first_name, second_name)
            self.staff_directory.append(new_staff)
            print ( '\n Staff {} {} has been successfully added \n' 
                .format(first_name, second_name))
                            
            print (self.assign_officespace(new_staff))
        elif position == "fellow":
            new_fellow = Fellow(first_name, second_name, wants_accomodation)
            self.fellows_directory.append(new_fellow)
            print ( '\n Fellow {} has been successfully added \n' .format(first_name))

            print (self.assign_officespace(new_fellow))
    
            try:
                if new_fellow.wants_accomodation.upper() == "Y":
                    print (self.assign_livingspace(new_fellow))
            except AttributeError:
                return
    def assign_officespace(self,new_person):
        available = []
        for office_space in self.office_directory:
            if len(office_space.occupants) < office_space.capacity:
                available.append(office_space)
        
        if available:
            allocated_room = random.choice(available)
            allocated_room.occupants.append(new_person)
            new_person.office = allocated_room.name
            self.status = True
            return ('\n {} has been allocated the office {} \n' 
                .format(new_person.name, allocated_room.name))
                        
    def assign_livingspace(self, new_person):
        available = []
        for living_space in self.livingspace_directory:
            if len(living_space.occupants) < living_space.capacity:
                available.append(living_space)

        if available:
            allocated_room= random.choice(available)
            allocated_room.occupants.append(new_person)
            new_person.livingspace = allocated_room.name
            self.status = True
            return ('\n {} has been allocated the livingspace {} \n' 
                .format(new_person.name, allocated_room.name))
                
                



