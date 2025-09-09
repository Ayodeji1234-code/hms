from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.scrollview import ScrollView
from kivy.uix.gridlayout import GridLayout

from operations.appointment import Appointment


class BookAppointmentScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = BoxLayout(orientation='vertical', padding=20, spacing=10)

        self.patient_input = TextInput(hint_text='Patient name', multiline=False)
        self.doctor_input = TextInput(hint_text='Doctor name', multiline=False)
        self.date_input = TextInput(hint_text='Date (YYYY/MM/DD)', multiline=False)
        self.time_input = TextInput(hint_text='Time (HH:MM)', multiline=False)

        self.result_label = Label(text='', size_hint_y=None, height=40)
        book_btn = Button(text='✅ Book Appointment')
        book_btn.bind(on_press=self.book_appointment)
        back_btn = Button(text='🔙 Back', on_press=self.go_back)

        layout.add_widget(Label(text='📅 Book Appointment', font_size=22))
        layout.add_widget(self.patient_input)
        layout.add_widget(self.doctor_input)
        layout.add_widget(self.date_input)
        layout.add_widget(self.time_input)
        layout.add_widget(book_btn)
        layout.add_widget(self.result_label)
        layout.add_widget(back_btn)

        self.add_widget(layout)

    def book_appointment(self, instance):
        patient = self.patient_input.text.strip()
        doctor = self.doctor_input.text.strip()
        date = self.date_input.text.strip()
        time = self.time_input.text.strip()
        if not all([patient, doctor, date, time]):
            self.result_label.text = "⚠️ Fill all fields!"
            return
        result = Appointment.book_appointment(patient, doctor, date, time)
        self.result_label.text = result

    def go_back(self, instance):
        self.manager.current = 'dashboard'
