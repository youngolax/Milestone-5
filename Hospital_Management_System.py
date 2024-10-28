# Staff class definition
class Staff:
    def __init__(self, staff_id, name, age, gender):
        self.staff_id = staff_id
        self.name = name
        self.age = age
        self.gender = gender

    def display_info(self):
        return f"Staff ID: {self.staff_id}, Name: {self.name}, Age: {self.age}, Gender: {self.gender}"

# Inheritance: A doctor inherits attributes of a staff
class Doctor(Staff):
    def __init__(self, staff_id, name, age, gender, speciality):
        super().__init__(staff_id, name, age, gender)
        self.speciality = speciality
        self.appointments = []
# Polymorphism: Method for adding a diagnosis is unique to doctors
    def diagnose(self, appointment, diagnosis):
        appointment.diagnosis = diagnosis

    def add_appointment(self, appointment):
        self.appointments.append(appointment)

    def treat_patient(self, patient):
        return f"{self.name} is treating patient {patient.name}."

# Inheritance: A nurse inherits attributes of class staff
class Nurse(Staff):
    def treat_patient(self, patient):
        return f"{self.name} is assisting in the treatment of patient {patient.name}."

class Patient:
    def __init__(self, patient_id, name, age, disease):
        self._patient_id = patient_id
        self.name = name
        self.age = age
        self.disease = disease

    def get_patient_details(self):
        return f"Name: {self.name}, Age: {self.age}, Disease: {self.disease}"

class Appointment:
    def __init__(self, appointment_id, patient, doctor, date):
        self.appointment_id = appointment_id
        self.patient = patient
        self.doctor = doctor
        self.date = date
        self.diagnosis = None

    def display_info(self):
        diagnosis = self.diagnosis if self.diagnosis else "Pending"
        return f"Appointment {self.appointment_id} - {self.date}  with Dr. {self.doctor.name}, Diagnosis: {diagnosis}"

class Billing:
    def __init__(self, billing_id, patient, amount):
        self.billing_id = billing_id
        self.patient = patient
        self.amount = amount

    def display_info(self):
        return f"Billing ID: {self.billing_id}, Patient: {self.patient.name}, Amount Due: UGX{self.amount}"


# Storing information
patients = {}
staff = {}
appointments = {}
billings = {}
appointment_counter = 1
billing_counter = 1

def add_patient():
    patient_id = input("Enter Patient ID: ")
    name = input("Enter Patient Name: ")
    age = input("Enter Patient Age: ")
    disease = input("Enter Patient Disease: ")
    patients[patient_id] = Patient(patient_id, name, age, disease)
    print(f"Patient {name} added successfully.\n")

def add_staff():
    staff_id = input("Enter Staff ID: ")
    name = input("Enter Staff Name: ")
    age = input("Enter Staff Age:")
    gender = input("Enter Staff Gender:")
    role = input("Enter Role (Doctor/Nurse): ").lower()

    if role == "doctor":
        speciality = input("Enter Doctor's Specialization: ")
        staff[staff_id] = Doctor(staff_id, name, age, gender, speciality)
    elif role == "nurse":
        staff[staff_id] = Nurse(staff_id, name, age, gender)
    else:
        print("Invalid role. Please enter 'Doctor' or 'Nurse'.\n")
        return
    print(f"{role.capitalize()} {name} added successfully.\n")

def create_appointment():
    global appointment_counter
    patient_id = input("Enter Patient ID for Appointment: ")
    doctor_id = input("Enter Doctor ID for Appointment: ")

    if patient_id not in patients:
        print("Patient not found.")
        return
    if doctor_id not in staff or not isinstance(staff[doctor_id], Doctor):
        print("Doctor not found.")
        return

    date = input("Enter Appointment Date (DD-MM-YYYY): ")
    appointment = Appointment(appointment_counter, patients[patient_id], staff[doctor_id], date)
    appointments[appointment_counter] = appointment
    staff[doctor_id].add_appointment(appointment)
    print(f"Appointment {appointment_counter} created successfully.\n")
    appointment_counter += 1

def assign_nurse():
    patient_id = input("Enter Patient ID: ")
    nurse_id = input("Enter Nurse ID: ")

    if patient_id not in patients:
        print("Patient not found.")
        return
    if nurse_id not in staff or not isinstance(staff[nurse_id], Nurse):
        print("Nurse not found.")
        return

    ward = input("Enter Ward for Nurse Assignment: ")
    print(f"Nurse {staff[nurse_id].name} assigned to patient {patients[patient_id].name} in ward {ward}.\n")

def make_diagnosis():
    appointment_id = int(input("Enter Appointment ID: "))
    if appointment_id not in appointments:
        print("Appointment not found.")
        return

    diagnosis = input("Enter Diagnosis: ")
    appointments[appointment_id].doctor.diagnose(appointments[appointment_id], diagnosis)
    print("Diagnosis recorded successfully.\n")

def generate_bill():
    global billing_counter
    patient_id = input("Enter Patient ID for Billing: ")
    if patient_id not in patients:
        print("Patient not found.")
        return
    amount = float(input("Enter Billing Amount: "))
    billing = Billing(billing_counter, patients[patient_id], amount)
    billings[billing_counter] = billing
    print(f"Bill {billing_counter} generated successfully.\n")
    billing_counter += 1

def view_records(record_type):
    if record_type == "patients":
        for patient in patients.values():
            print(patient.get_patient_details())
    elif record_type == "staff":
        for member in staff.values():
            print(member.display_info())
    elif record_type == "appointments":
        for appointment in appointments.values():
            print(appointment.display_info())
    elif record_type == "bills":
        for bill in billings.values():
            print(bill.display_info())
    else:
        print("Invalid record type.")
    print()

# Main program loop
def main():
    while True:
        print("Hospital Management System")
        print("1. Add New Patient")
        print("2. Add New Staff (Doctor/Nurse)")
        print("3. Create Appointment")
        print("4. Assign Nurse to Patient")
        print("5. Make a Diagnosis")
        print("6. Generate Bill")
        print("7. View Records (Patients, Staff, Appointments, Bills)")
        print("8. Exit")

        choice = input("Enter your choice: ")
        if choice == "1":
            add_patient()
        elif choice == "2":
            add_staff()
        elif choice == "3":
            create_appointment()
        elif choice == "4":
            assign_nurse()
        elif choice == "5":
            make_diagnosis()
        elif choice == "6":
            generate_bill()
        elif choice == "7":
            record_type = input("Enter record type to view (patients, staff, appointments, bills): ").lower()
            view_records(record_type)
        elif choice == "8":
            print("Exiting Hospital Management System. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
