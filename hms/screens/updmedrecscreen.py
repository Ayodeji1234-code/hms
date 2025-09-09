from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.scrollview import ScrollView
from operations.medicalrecord import MedicalRecord 

class UpdateMedicalRecordScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        layout = BoxLayout(orientation='vertical', spacing=10, padding=20)

        self.patient_input = TextInput(hint_text="Enter patient's name", multiline=False)
        self.date_input = TextInput(hint_text="Enter date (YYYY/MM/DD)", multiline=False)
        self.diagnosis_input = TextInput(hint_text="Enter diagnosis", multiline=True)
        self.treatment_input = TextInput(hint_text="Enter treatment", multiline=True)

        self.message_label = Label(text='', color=(1, 0, 0, 1), size_hint=(1, 0.2))

        update_button = Button(text="Update Record", size_hint=(1, 0.2))
        update_button.bind(on_press=self.update_record)

        layout.add_widget(Label(text="Update Medical Record", font_size=20, size_hint=(1, 0.2)))
        layout.add_widget(self.patient_input)
        layout.add_widget(self.date_input)
        layout.add_widget(self.diagnosis_input)
        layout.add_widget(self.treatment_input)
        layout.add_widget(update_button)
        back_btn = Button(text="Back", size_hint=(1, 0.2))
        back_btn.bind(on_press=self.go_back)
        layout.add_widget(back_btn)

        layout.add_widget(self.message_label)

        self.add_widget(layout)

    def update_record(self, instance):
        patient_name = self.patient_input.text.strip().lower()
        date = self.date_input.text.strip()
        diagnosis = self.diagnosis_input.text.strip()
        treatment = self.treatment_input.text.strip()

        if not all([patient_name, date, diagnosis, treatment]):
            self.message_label.text = "All fields are required."
            return

        if patient_name not in MedicalRecord.records_for_doctor: #checks if patient's record exist already
            self.message_label.text = "No record found for that patient."
            return

        # Perform the update
        MedicalRecord.records_for_doctor[patient_name].append({
            "date": date,
            "diagnosis": diagnosis,
            "treatment": treatment
        })

        self.message_label.text = "Record updated successfully."
        # Optional: Clear inputs
        self.patient_input.text = ''
        self.date_input.text = ''
        self.diagnosis_input.text = ''
        self.treatment_input.text = ''

    def go_back(self, instance):
        # Switch back to your main menu or previous screen
        self.manager.current = 'dashboard'
