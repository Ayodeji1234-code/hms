import sys
sys.path.append(r'C:\Users\user\Documents\python')
from users.user import User
import authentication as auth2
from operations.appointment import Appointment


class Admin(User):
    def __init__(self,username,name):
        super().__init__(username,name,role = 'admin')

    def dashboard(self):
        print(f'{self.name} dashboard')
        print('0. See Dashboard')
        print('1. Register User')
        print('2. List Users')
        print('3. Delete User')
        print('4. View system Reports')

    def register_user(self):
        username = input("Choose a username: ").strip()
        if username in auth2.USERS:
            print("Username already exists.")
            return

        password = input("Enter password: ").strip()
        name = input("Full name: ").strip()
        role = input("Role (doctor/patient/admin): ").lower()

        if role not in ('doctor', 'patient', 'admin'):
            print("Invalid role.")
            return

        auth2.USERS[username] = {
            'password': password,
            'name': name,
            'role': role
        }
        print(" User registered.")
        print(f'Userame : {username} | Password : {password} | Role : {role} | Name : {name}')  

    def list_users(self):
        if not auth2.USERS:
            print("⚠️ No users registered.")
            return
        print("\n Registered Users:")
        for username, info in auth2.USERS.items():
            print(f"Username: {username} | Name: {info['name']} | Role: {info['role']}")
    
    def delete_user(self):
        username = input("Enter username to delete: ").strip()
        if username in auth2.USERS:
            del auth2.USERS[username]
            print(f" User '{username}' deleted.")
        else:
            print(" User not found.")

    def generate_report(self):
        total_users = len(auth2.USERS)
        roles = {'doctor': 0, 'patient': 0, 'admin': 0}
        for user in auth2.USERS.values():
            role = user.get('role')
            if role in roles:
                roles[role] += 1

        total_appointments = len(Appointment.appointments)
        status_counts = {'Scheduled': 0, 'Completed': 0, 'Cancelled': 0}

        for appt in Appointment.appointments:
            status = appt.get('status', 'Scheduled')
            if status in status_counts:
                status_counts[status] += 1
            else:
                status_counts[status] = 1

        print("\n📊 SYSTEM REPORT")
        print("-" * 40)
        print(f"Total Users: {total_users}")
        print(f"  Doctors: {roles['doctor']}")
        print(f"  Patients: {roles['patient']}")
        print(f"  Admins: {roles['admin']}")
        print()
        print(f"Total Appointments: {total_appointments}")
        for status, count in status_counts.items():
            print(f"  {status}: {count}")
        print("-" * 40)        
        

    def action(self,choice:str):
        if choice == '1':
            self.register_user()
        elif choice == '2':
            self.list_users()
        elif choice == '3':
            self.delete_user()
        elif choice == '4':
            self.generate_report()
        elif choice == '0':
            self.dashboard() 
        else:
            print('Invalid Choice')
                 
