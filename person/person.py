class Person(object):
    def __init__(self, name):
        self.name = name
    
class Staff(Person):
    def __init__(self, name):
        self.name = name
        self.position = 'staff'
        self.livingspace = 'N'

class Fellow(Person):
    def __init__(self, name, livingspace='N'):
        self.name = name
        self.position = 'fellow'
        if livingspace:
            self.livingspace = livingspace

