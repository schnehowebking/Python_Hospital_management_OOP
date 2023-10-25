import random

class Appointment:
    def __init__(self, patient, doctor, date, time):
        self.appointment_id = random.randint(100000, 999999)
        self.patient = patient
        self.doctor = doctor
        self.date = date
        self.time = time
        self.status = "Scheduled"
