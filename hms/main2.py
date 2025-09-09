from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
import authentication as auth5
from screens.bookappscreen import BookAppointmentScreen
from screens.cancelappscreen import CancelAppointmentScreen
from screens.viewappscreen import ViewAppointmentsScreen
from screens.createrecscreen import CreateRecordScreen
from screens.regscreen import RegisterUserScreen
from screens.listscreen import ListUsersScreen
from screens.viewmedrecscreen import ViewRecordScreen
from screens.updmedrecscreen import UpdateMedicalRecordScreen
from screens.sysrepscreen import SystemReportScreen

class LoginScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = BoxLayout(orientation='vertical', padding=10, spacing=5)

        self.username_input = TextInput(hint_text='Username', multiline=False)
        self.password_input = TextInput(hint_text='Password', multiline=False, password=True)
        self.message_label = Label(text='')

        login_button = Button(text='Login', size_hint=(1, 0.3))
        login_button.bind(on_press=self.try_login)

        self.username_input.size_hint = (1, 0.2)
        self.password_input.size_hint = (1, 0.2)

        layout.add_widget(Label(text="Hospital Management Login", font_size=24))
        layout.add_widget(self.username_input)
        layout.add_widget(self.password_input)
        layout.add_widget(login_button)
        layout.add_widget(self.message_label)

        self.add_widget(layout)

    def try_login(self, instance):
        username = self.username_input.text.strip()
        password = self.password_input.text.strip()
        user = auth5.login(username, password)  # Modify login to accept parameters
        if not user:
            self.message_label.text = 'Invalid password or username'
            return

        if user.role == "doctor":
            dashboard = DoctorDashboard(name='dashboard')
        elif user.role == 'admin':
            dashboard = AdminDashboard(name='dashboard')    
        else:
            dashboard = PatientDashboard(name='dashboard')

        dashboard.set_user(user)

        if self.manager.has_screen('dashboard'):
            old_dashboard = self.manager.get_screen('dashboard')
            self.manager.remove_widget(old_dashboard)
        self.manager.add_widget(dashboard)    # add to screen manager and switch
        self.manager.current = 'dashboard'


class DoctorDashboard(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = BoxLayout(orientation='vertical', padding=20, spacing=10)
        self.welcome_label = Label(text='Welcome, doctor!', font_size=20)
        layout.add_widget(self.welcome_label)
        
        view_btn = Button(text='View Appointments')
        view_btn.bind(on_press=self.go_view)
        layout.add_widget(view_btn)

        create_btn = Button(text='Create Medical Record')
        create_btn.bind(on_press=self.go_create)
        layout.add_widget(create_btn)
        
        update_btn = Button(text ='Upadte Medical Record')
        update_btn.bind(on_press = self.go_update)
        layout.add_widget(update_btn)
        
        records_btn = Button(text='View Medical Records')
        records_btn.bind(on_press=self.view_medrec)
        layout.add_widget(records_btn)

        logout_button = Button(text='Logout', size_hint=(1, 0.3))
        logout_button.bind(on_press=self.logout)
        layout.add_widget(logout_button)
        self.add_widget(layout)

    def logout(self,instance):
        self.user = None
        self.manager.current = 'login'    
            

    def set_user(self, user):
        self.user = user
        self.welcome_label.text = f"Welcome, {user.name}! ({user.role})" 

    def go_view(self, instance):
        self.manager.current = 'view_appointments'    

    def go_create(self,instance):
        self.manager.current = 'create_record'   

    def view_medrec(self,instance):
        self.manager.current = 'view_medrec'   

    def go_update(self,instance):
        self.manager.current = 'update_record'      
           

class PatientDashboard(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = BoxLayout(orientation='vertical', padding=20, spacing=10)

        self.welcome_label = Label(text='Welcome, patient!', font_size=20)
        layout.add_widget(self.welcome_label)

        # Book Appointment button
        book_btn = Button(text='Book Appointment')
        book_btn.bind(on_press=self.go_book)
        layout.add_widget(book_btn)

        # Cancel Appointment button
        cancel_btn = Button(text='Cancel Appointment')
        cancel_btn.bind(on_press=self.go_cancel)
        layout.add_widget(cancel_btn)

        # View Appointments button
        view_btn = Button(text='View Appointments')
        view_btn.bind(on_press=self.go_view)
        layout.add_widget(view_btn)

        # View Medical Records button
        records_btn = Button(text='View Medical Records')
        records_btn.bind(on_press=self.view_medrec)
        layout.add_widget(records_btn)

        logout_button = Button(text='Logout', size_hint=(1, 0.3))
        logout_button.bind(on_press=self.logout)
        layout.add_widget(logout_button)
        self.add_widget(layout)

    def logout(self,instance):
        self.user = None
        self.manager.current = 'login'     


    def set_user(self, user):
        self.user = user
        self.welcome_label.text = f"Welcome, {user.name}! ({user.role})"

    def go_book(self, instance):
        # This name must match what you used in ScreenManager
        self.manager.current = 'book_appointment'

    def go_cancel(self, instance):
        self.manager.current = 'cancel_appointment'

    def go_view(self, instance):
        self.manager.current = 'view_appointments'

    def view_medrec(self,instance):
        self.manager.current = 'view_medrec'     
               

class AdminDashboard(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = BoxLayout(orientation='vertical', padding=20, spacing=10)
        self.welcome_label = Label(text='Welcome, Admin!', font_size=20)
        layout.add_widget(self.welcome_label)

        reg_btn = Button(text='Register User')
        reg_btn.bind(on_press=self.reg)
        layout.add_widget(reg_btn)

        list_btn = Button(text='List users')
        list_btn.bind(on_press=self.list)
        layout.add_widget(list_btn)

        rep_btn = Button(text='View System Reports')
        rep_btn.bind(on_press=self.report)
        layout.add_widget(rep_btn)
        
        logout_button = Button(text='Logout', size_hint=(1, 0.3))
        logout_button.bind(on_press=self.logout)
        layout.add_widget(logout_button)
        self.add_widget(layout)

    def logout(self,instance):
        self.user = None
        self.manager.current = 'login'    

    def set_user(self, user):
        self.user = user
        self.welcome_label.text = f"Welcome, {user.name}! ({user.role})"    

    def reg(self,instance):
        self.manager.current = 'register_user'  

    def list(self,instance):
        self.manager.current = 'list_users'  

    def report(self,instance):
        self.manager.current = 'generate_report'        

class HospitalApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(LoginScreen(name='login'))
        sm.add_widget(BookAppointmentScreen(name='book_appointment'))
        sm.add_widget(CancelAppointmentScreen(name='cancel_appointment'))
        sm.add_widget(ViewAppointmentsScreen(name='view_appointments'))
        sm.add_widget(CreateRecordScreen(name='create_record'))
        sm.add_widget(RegisterUserScreen(name='register_user'))
        sm.add_widget(ListUsersScreen(name='list_users'))
        sm.add_widget(ViewRecordScreen(name='view_medrec'))
        sm.add_widget(UpdateMedicalRecordScreen(name='update_record'))
        sm.add_widget(SystemReportScreen(name='generate_report'))
        return sm

if __name__ == '__main__':
    HospitalApp().run()
