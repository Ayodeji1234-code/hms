from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button

from authentication import USERS as auth_users
from operations.appointment import Appointment

class SystemReportScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.main_layout = BoxLayout(orientation='vertical', spacing=10, padding=20)
        self.report_labels = []

        # Title
        self.main_layout.add_widget(Label(text="📊 SYSTEM REPORT", font_size=24, bold=True))

        self.report_container = BoxLayout(orientation='vertical', spacing=10)
        self.main_layout.add_widget(self.report_container)

        # Refresh button
        refresh_btn = Button(text="🔄 Refresh Report", size_hint=(1, 0.1))
        refresh_btn.bind(on_press=self.generate_report)
        self.main_layout.add_widget(refresh_btn)

        # Back button
        back_btn = Button(text="🔙 Back to Dashboard", size_hint=(1, 0.1))
        back_btn.bind(on_press=self.go_back)
        self.main_layout.add_widget(back_btn)

        self.add_widget(self.main_layout)
        self.generate_report()  # Generate on screen load

    def generate_report(self, instance=None):
        # Clear previous report
        self.report_container.clear_widgets()

        total_users = len(auth_users)
        roles = {'doctor': 0, 'patient': 0, 'admin': 0}
        for user in auth_users.values():
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

        # Display user stats
        self.report_container.add_widget(Label(text=f"👥 Total Users: {total_users}"))
        self.report_container.add_widget(Label(text=f"   🥼 Doctors: {roles['doctor']}"))
        self.report_container.add_widget(Label(text=f"   🧍 Patients: {roles['patient']}"))
        self.report_container.add_widget(Label(text=f"   🛡️ Admins: {roles['admin']}"))

        self.report_container.add_widget(Label(text=""))

        # Display appointment stats
        self.report_container.add_widget(Label(text=f"📅 Total Appointments: {total_appointments}"))
        for status, count in status_counts.items():
            self.report_container.add_widget(Label(text=f"   📌 {status}: {count}"))

    def go_back(self, instance):
        self.manager.current = 'dashboard'
