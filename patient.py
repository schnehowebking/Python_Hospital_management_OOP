import secrets

class Patient:
    def __init__(self, name, age, medical_history, contact_info):
        self.patient_id = secrets.SystemRandom().randint(1000, 9999)
        self.name = name
        self.age = age
        self.medical_history = medical_history
        self.contact_info = contact_info
