from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from operations.medicalrecord import MedicalRecord  # import your class

class CreateRecordScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        # Main vertical layout
        layout = BoxLayout(orientation='vertical', padding=20, spacing=15)

        # Patient name
        self.patient_input = TextInput(hint_text="Enter patient name", multiline=False)
        layout.add_widget(Label(text="Patient Name:"))
        layout.add_widget(self.patient_input)

        # Date
        self.date_input = TextInput(hint_text="YYYY/MM/DD", multiline=False)
        layout.add_widget(Label(text="Date:"))
        layout.add_widget(self.date_input)

        # Diagnosis
        self.diagnosis_input = TextInput(hint_text="Enter diagnosis", multiline=False)
        layout.add_widget(Label(text="Diagnosis:"))
        layout.add_widget(self.diagnosis_input)

        # Treatment
        self.treatment_input = TextInput(hint_text="Enter treatment", multiline=False)
        layout.add_widget(Label(text="Treatment:"))
        layout.add_widget(self.treatment_input)

        # Submit button
        submit_btn = Button(text="Create Record", size_hint=(1, 0.2))
        submit_btn.bind(on_press=self.create_record)
        layout.add_widget(submit_btn)

        # Back button (optional)
        back_btn = Button(text="Back", size_hint=(1, 0.2))
        back_btn.bind(on_press=self.go_back)
        layout.add_widget(back_btn)

        self.add_widget(layout)

    def create_record(self, instance):
        patient = self.patient_input.text.strip().lower()
        date = self.date_input.text.strip()
        diagnosis = self.diagnosis_input.text.strip()
        treatment = self.treatment_input.text.strip()

        if not patient or not date or not diagnosis or not treatment:
            print("⚠️ All fields are required!")
            return

        MedicalRecord.records_for_doctor[patient].append({
            'date': date,
            'diagnosis': diagnosis,
            'treatment': treatment
        })
        print(f"✅ Medical record created for {patient}")
        # Clear inputs
        self.patient_input.text = ""
        self.date_input.text = ""
        self.diagnosis_input.text = ""
        self.treatment_input.text = ""

    def go_back(self, instance):
        # Switch back to your main menu or previous screen
        self.manager.current = 'dashboard'  
