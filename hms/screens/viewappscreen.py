from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.scrollview import ScrollView
from kivy.uix.gridlayout import GridLayout

from operations.appointment import Appointment

class ViewAppointmentsScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        main_layout = BoxLayout(orientation='vertical', padding=20, spacing=10)

        # Title
        main_layout.add_widget(Label(text="📋 View Appointments", font_size=22))

        # Input for username
        self.name_input = TextInput(hint_text='Enter Patient name', multiline=False)
        main_layout.add_widget(self.name_input)

        # Button to load appointments
        view_btn = Button(text='🔍 View Appointments')
        view_btn.bind(on_press=self.view_appointments)
        main_layout.add_widget(view_btn)

        # Scrollable area for appointment list
        self.scroll = ScrollView(size_hint=(1, 1))
        self.appointment_list = GridLayout(cols=1, size_hint_y=None, spacing=5, padding=10)
        self.appointment_list.bind(minimum_height=self.appointment_list.setter('height'))
        self.scroll.add_widget(self.appointment_list)

        main_layout.add_widget(self.scroll)

        # Back button
        back_btn = Button(text='🔙 Back')
        back_btn.bind(on_press=self.go_back)
        main_layout.add_widget(back_btn)

        self.add_widget(main_layout)

    def view_appointments(self, instance):
        name = self.name_input.text.strip()
        self.appointment_list.clear_widgets()

        if not name:
            self.appointment_list.add_widget(Label(text="⚠️ Please enter a username."))
            return

        # Fetch appointments from your Appointment class
        found = False
        for appt in Appointment.appointments:
            if appt['patient'] == name:
                found = True
                info = (f"ID: {appt['id']} | Date: {appt['date']} | Time: {appt['time']} | "
                        f"Doctor: {appt['doctor']} | Status: {appt['status']}")
                self.appointment_list.add_widget(Label(text=info, size_hint_y=None, height=30))

        if not found:
            self.appointment_list.add_widget(Label(text="❌ No appointments found."))

    def go_back(self, instance):
        self.manager.current = 'dashboard'
