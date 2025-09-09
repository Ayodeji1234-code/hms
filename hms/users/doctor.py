import sys
sys.path.append(r'C:\Users\user\Documents\python')
from users.user import User
from operations.appointment import Appointment


class Doctor(User):
    def __init__(self,username,name):
        super().__init__(username,name,role = 'doctor')

    def dashboard(self):
        print(f'{self.name} dashboard')
        print('0. See Dashboard')
        print('1. View Appointmeent')
        print('2. Access Patient record')
        print('3. Create Record')
        print('4. Update Record')
       
    def action(self,choice:str):  
        from operations.medicalrecord import MedicalRecord
        if choice == '1':
           Appointment.view_appointment(self.username)
        elif choice == '2':
           patient_name = input('Enter patient name: ').strip().lower()
           MedicalRecord.view_medrec(patient_name)
           MedicalRecord.view_all_rec()
        elif choice == '3':
           patient_name = input('Enter patient name: ')
           MedicalRecord.create_record()
        elif choice == '4':
           MedicalRecord.update_record()
        elif choice == '0':
           self.dashboard()
        else:
           print('Invalid Choice')
              

  
           

            

    