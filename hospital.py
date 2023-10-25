from appointment import Appointment


class Hospital:
    def __init__(self, name):
        self.name = name
        self.patients = []
        self.doctors = []
        self.appointments = []

    def add_patient(self, patient):
        self.patients.append(patient)

    def add_doctor(self, doctor):
        self.doctors.append(doctor)

    def schedule_appointment(self, patient, doctor, date, time):
        appointment = Appointment(patient, doctor, date, time)
        self.appointments.append(appointment)

    def update_appointment_status(self, appointment_id, new_status):
        for appointment in self.appointments:
            if appointment.appointment_id == appointment_id:
                appointment.status = new_status

    def list_doctor_appointments(self, doctor):
        doctor_appointments = [appointment for appointment in self.appointments if appointment.doctor == doctor]
        return doctor_appointments

    def list_patient_appointments(self, patient):
        patient_appointments = [appointment for appointment in self.appointments if appointment.patient == patient]
        return patient_appointments
