import random

class Doctor:
    def __init__(self, name, specialization, contact_info):
        self.doctor_id = random.randint(10000, 99999)
        self.name = name
        self.specialization = specialization
        self.contact_info = contact_info
