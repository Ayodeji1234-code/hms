from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

from operations.appointment import Appointment 

class CancelAppointmentScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        layout = BoxLayout(orientation='vertical', padding=20, spacing=10)

        # Title
        layout.add_widget(Label(text='Cancel Appointment', font_size=22))

        # Input for appointment ID
        self.appt_id_input = TextInput(
            hint_text='Enter Appointment ID to cancel',
            multiline=False)
        self.appt_username_input = TextInput(
            hint_text='Enter name to cancel',
            multiline=False)
        layout.add_widget(self.appt_id_input)
        layout.add_widget(self.appt_username_input)

        # Result label
        self.result_label = Label(text='', size_hint_y=None, height=40)
        layout.add_widget(self.result_label)

        # Buttons
        cancel_btn = Button(text='Cancel Appointment')
        cancel_btn.bind(on_press=self.cancel_appointment)
        layout.add_widget(cancel_btn)

        back_btn = Button(text='🔙 Back to Dashboard')
        back_btn.bind(on_press=self.go_back)
        layout.add_widget(back_btn)

        self.add_widget(layout)

    def cancel_appointment(self, instance):
        appt_id = self.appt_id_input.text.strip()
        username = self.appt_username_input.text.strip()  # 👈 get username from input box

        if not appt_id or not username:
            self.result_label.text = "Please enter both Appointment ID and Username."
            return

        # Call backend cancel method
        result = Appointment.cancel_appointment(appt_id,username)
        self.result_label.text = result

    def go_back(self, instance):
        self.manager.current = 'dashboard'
