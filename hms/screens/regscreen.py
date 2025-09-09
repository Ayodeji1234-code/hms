from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from authentication import USERS # import your class

class RegisterUserScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        # Main vertical layout
        layout = BoxLayout(orientation='vertical', padding=20, spacing=15)

        #Users name
        self.name_input = TextInput(hint_text="Enter user's name", multiline=False)
        layout.add_widget(Label(text="User's Name:"))
        layout.add_widget(self.name_input)

        #Username
        self.username_input = TextInput(hint_text="Enter Username", multiline=False)
        layout.add_widget(Label(text="Username:"))
        layout.add_widget(self.username_input)

        # Role
        self.role_input = TextInput(hint_text="Enter role", multiline=False)
        layout.add_widget(Label(text="role:"))
        layout.add_widget(self.role_input)

        # password
        self.password_input = TextInput(hint_text="Enter password", multiline=False, password = True)
        layout.add_widget(Label(text="password:"))
        layout.add_widget(self.password_input)

        # Submit button
        submit_btn = Button(text="Register User", size_hint=(1, 0.2))
        submit_btn.bind(on_press=self.register_user)
        layout.add_widget(submit_btn)

        # Back button (optional)
        back_btn = Button(text="Back", size_hint=(1, 0.2))
        back_btn.bind(on_press=self.go_back)
        layout.add_widget(back_btn)

        self.add_widget(layout)

    def register_user(self, instance):
        name = self.name_input.text.strip().lower()
        username = self.username_input.text.strip()
        role = self.role_input.text.strip()
        password = self.password_input.text.strip()

        if not name or not username or not role or not password:
            print("All fields are required")
            return

        if username in USERS:
            print("Username already exists")
            return

        USERS[username] = ({
            'name': name,
            'role': role,
            'password': password
        })
        print(f"User Registered Successfully")
        # Clear inputs
        self.name_input.text = ""
        self.username_input.text = ""
        self.role_input.text = ""
        self.password_input.text = ""

    def go_back(self, instance):
        # Switch back to your main menu or previous screen
        self.manager.current = 'dashboard'  # make sure you have a 'main' screen in ScreenManager
