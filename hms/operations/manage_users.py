import sys
sys.path.append(r'C:\Users\user\Documents\python')
import authentication as auth2  #USERS is a dict

class ManageUsers:
    @staticmethod
    def register_user():
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

    @staticmethod
    def list_users():
        if not auth2.USERS:
            print("⚠️ No users registered.")
            return
        print("\n Registered Users:")
        for username, info in auth2.USERS.items():
            print(f"Username: {username} | Name: {info['name']} | Role: {info['role']}")
    
    @staticmethod
    def delete_user():
        username = input("Enter username to delete: ").strip()
        if username in auth2.USERS:
            del auth2.USERS[username]
            print(f" User '{username}' deleted.")
        else:
            print(" User not found.")
    