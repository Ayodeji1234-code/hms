import sys
sys.path.append(r'C:\Users\user\Documents\python')
from collections import defaultdict
import authentication as auth4

class MedicalRecord:
    records_for_doctor : dict[str,list[dict]]= defaultdict(list)

    @staticmethod
    def view_medrec(patient_name : str):
        patient_key = patient_name.strip().lower()
        print(f'Medical record for {patient_name}')
        records = MedicalRecord.records_for_doctor
        if patient_key in records:
            patient_data = records[patient_key]
            for medrec in patient_data:
                print(f"Date: {medrec['date']} | Diagnosis: {medrec['diagnosis']} | Treatment: {medrec['treatment']}") 
        else:
            print("No medical records found.")

    @staticmethod
    def view_all_rec():
        names =list( MedicalRecord.records_for_doctor.keys()) 
        for patient in names:
            print(f'Medical record for {patient}')
            patient_data = MedicalRecord.records_for_doctor[patient]
            for medrec in patient_data:
                print(f"Date: {medrec['date']} | Diagnosis: {medrec['diagnosis']} | Treatment: {medrec['treatment']}") 
            print('\n\n')

    @staticmethod
    def patient_view_rec():
        patient = input('Enter username: ')
        if patient in auth4.USERS:
            password = input('Enter password: ')
            if password == auth4.USERS[patient]['password']:
                name = auth4.USERS[patient]['name']
                MedicalRecord.view_medrec(name)      
                

    @staticmethod
    def create_record():
        patient: str = input('Enter patient name: ').lower().strip()
        date = input('Enter date (YYYY/MM/DD): ')
        diagnosis = input('Enter diagnosis: ')
        treatment = input('Enter treatment: ')

        MedicalRecord.records_for_doctor[patient].append( { 
                        'date' : date,
                        'diagnosis' : diagnosis,
                        'treatment' : treatment
                        })
        print('Medical record created succesfully')

    @staticmethod
    def update_record():   
        patient_name = input("Enter patient's name: ").strip().lower()

        if patient_name not in MedicalRecord.records_for_doctor:
            print('No existing record found for patient')
            return

        date = input("Enter date (YYYY/MM/DD): ").strip()
        diagnosis = input("Enter diagnosis: ").strip()
        treatment = input("Enter treatment: ").strip()

        if not diagnosis or not treatment:
            raise ValueError("Diagnosis and treatment cannot be empty.")

        MedicalRecord.records_for_doctor[patient_name].append({
            'date': date,
            'diagnosis': diagnosis,
            'treatment': treatment
        })
        print('Medical record updated successfully')

        print("\n✅ New medical record added:")
        print(f"  Patient : {patient_name} | Date : {date} | Diagnosis : {diagnosis} | Treatment : {treatment}")
    
    

    
