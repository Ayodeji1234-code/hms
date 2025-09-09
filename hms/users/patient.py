import sys
sys.path.append(r'C:\Users\user\Documents\python')
from users.user import User
from operations.appointment import Appointment


class Patient(User):
    def __init__(self,username,name):
        super().__init__(username,name,role = 'patient')

    def dashboard(self):
        print(f'{self.name} dashboard')
        print('0. See Dashboard')
        print('1. Book Appointment')
        print('2. View Appointment')
        print('3. Cancel Appointment')
        print('4. View Medical History')
        
    def action(self,choice:str):    
        from operations.medicalrecord import MedicalRecord  
        if choice == '1':
           doctor = input("Enter doctor's username: ")
           Appointment.book_appointment(self.username,doctor)
        elif choice == '2':
           Appointment.view_appointment(self.username)
        elif choice == '3':
           appointment_id = input("Enter appointment ID to cancel: ")
           Appointment.cancel_appointment(appointment_id,self.username)
        elif choice == '4':
           MedicalRecord.patient_view_rec()
        elif choice == '0':
           self.dashboard() 
        else:
           print('Invalid Choice')
           