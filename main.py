from patient import Patient
from doctor import Doctor
from hospital import Hospital

# Create a hospital
my_hospital = Hospital("General Hospital")

# Function to display menu
def display_menu():
    print("\nHospital Management System Menu:")
    print("1. Add Patient")
    print("2. Add Doctor")
    print("3. Schedule Appointment")
    print("4. Update Appointment Status")
    print("5. List Doctor's Appointments")
    print("6. List Patient's Appointments")
    print("7. Exit")

# Main loop
while True:
    display_menu()

    if (choice := input("Enter your choice: ")) == "1":
        name = input("Enter patient name: ")
        age = int(input("Enter patient age: "))
        medical_history = input("Enter medical history: ")
        contact_info = input("Enter contact info: ")
        patient = Patient(name, age, medical_history, contact_info)
        my_hospital.add_patient(patient)
        print(f'Patient {patient.patient_id} added successfully.')

    elif choice == "2":
        name = input("Enter doctor name: ")
        specialization = input("Enter doctor specialization: ")
        contact_info = input("Enter contact info: ")
        doctor = Doctor(name, specialization, contact_info)
        my_hospital.add_doctor(doctor)
        print(f"Doctor {doctor.doctor_id} added successfully.")

    elif choice == "3":
        patient_id = int(input("Enter patient ID: "))
        doctor_id = int(input("Enter doctor ID: "))
        date = input("Enter date (YYYY-MM-DD): ")
        time = input("Enter time: ")
        patient = next((p for p in my_hospital.patients if p.patient_id == patient_id), None)
        doctor = next((d for d in my_hospital.doctors if d.doctor_id == doctor_id), None)
        if patient and doctor:
            my_hospital.schedule_appointment(patient, doctor, date, time)
            print("Appointment scheduled successfully.")
        else:
            print("Patient or doctor not found.")

    elif choice == "4":
        appointment_id = int(input("Enter appointment ID: "))
        new_status = input("Enter new status: ")
        my_hospital.update_appointment_status(appointment_id, new_status)
        print("Appointment status updated successfully.")

    elif choice == "5":
        doctor_id = int(input("Enter doctor ID: "))
        doctor = next((d for d in my_hospital.doctors if d.doctor_id == doctor_id), None)
        if doctor:
            doctor_appointments = my_hospital.list_doctor_appointments(doctor)
            for appointment in doctor_appointments:
                print(f"Appointment ID: {appointment.appointment_id}, Date: {appointment.date}, Time: {appointment.time}, Status: {appointment.status}")
        else:
            print("Doctor not found.")

    elif choice == "6":
        patient_id = int(input("Enter patient ID: "))
        patient = next((p for p in my_hospital.patients if p.patient_id == patient_id), None)
        if patient:
            patient_appointments = my_hospital.list_patient_appointments(patient)
            for appointment in patient_appointments:
                print(f"Appointment ID: {appointment.appointment_id}, Date: {appointment.date}, Time: {appointment.time}, Status: {appointment.status}")
        else:
            print("Patient not found.")

    elif choice == "7":
        break
