import sys
sys.path.append(r'C:\Users\user\Documents\python')
from users.doctor import Doctor
from users.patient import Patient

USERS = {
    'dr_mike':{'password':'doctor123','role':'doctor','name':'Dr. Michael'},
    'Esther' :{'password':'esther123','role':'patient','name':'Miss Esther'},
    'Qahar' :{'password':'qahar123','role':'admin','name':'Mr Qahar'}
}
def login(username : str , password : str):
    from users.admin import Admin

    user_data = USERS.get(username)
    if user_data and user_data['password'] == password:
        role = user_data['role']
        name = user_data['name']

        if role == 'doctor':
          return Doctor(username,name)
        elif role == 'patient':
          return Patient(username,name)
        elif role == 'admin':
          return Admin(username,name)
        else:
          print('Invalid input')
          return None    
    else:
      print('Invalid username or password. Try again.')