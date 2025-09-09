from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.scrollview import ScrollView
from kivy.uix.gridlayout import GridLayout

from operations.medicalrecord import MedicalRecord

class ViewRecordScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        main_layout = BoxLayout(orientation='vertical', padding=20, spacing=10)

        # Title
        main_layout.add_widget(Label(text="📋 View Medical Records", font_size=22))

        # Input for username
        self.name_input = TextInput(hint_text='Enter Patient name', multiline=False)
        main_layout.add_widget(self.name_input)

        # Button to load appointments
        view_btn = Button(text='🔍 View Medical Records')
        view_btn.bind(on_press=self.view_records)
        main_layout.add_widget(view_btn)

        # Scrollable area for appointment list
        self.scroll = ScrollView(size_hint=(1, 1))
        self.record_list = GridLayout(cols=1, size_hint_y=None, spacing=5, padding=10)
        self.record_list.bind(minimum_height=self.record_list.setter('height'))
        self.scroll.add_widget(self.record_list)

        main_layout.add_widget(self.scroll)

        # Back button
        back_btn = Button(text='🔙 Back')
        back_btn.bind(on_press=self.go_back)
        main_layout.add_widget(back_btn)

        self.add_widget(main_layout)

    def view_records(self, instance):
        name = self.name_input.text.strip().lower()
        self.record_list.clear_widgets()

        if not name:
            self.record_list.add_widget(Label(text="⚠️ Please enter a name."))
            return

    # Get the list of records for the patient
        patient_records = MedicalRecord.records_for_doctor.get(name, [])

        if not patient_records:
            self.record_list.add_widget(Label(text=" No medical records found."))
            return

        for medrec in patient_records:
            info = f"Date: {medrec['date']} | Diagnosis: {medrec['diagnosis']} | Treatment: {medrec['treatment']}"
            self.record_list.add_widget(Label(text=info, size_hint_y=None, height=30))

    def go_back(self, instance):
        self.manager.current = 'dashboard'
