from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.scrollview import ScrollView
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from authentication import USERS  

class ListUsersScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        main_layout = BoxLayout(orientation='vertical', padding=10, spacing=10)

        title = Label(text="Registered Users", font_size=24, size_hint=(1, 0.1))
        main_layout.add_widget(title)

        # Scrollable user list
        scroll_view = ScrollView(size_hint=(1, 0.8))
        self.users_layout = GridLayout(cols=1, spacing=10, size_hint_y=None)
        self.users_layout.bind(minimum_height=self.users_layout.setter('height'))

        scroll_view.add_widget(self.users_layout)
        main_layout.add_widget(scroll_view)

        # Back button
        back_btn = Button(text="Back", size_hint=(1, 0.1))
        back_btn.bind(on_press=self.go_back)
        main_layout.add_widget(back_btn)

        self.add_widget(main_layout)

    def on_pre_enter(self):
        self.load_users()

    def load_users(self):
        self.users_layout.clear_widgets()

        if not USERS:
            self.users_layout.add_widget(Label(text="No users registered yet."))
            return

        for username, data in USERS.items():
            # Create horizontal box for each user
            user_box = BoxLayout(orientation='horizontal', size_hint_y=None, height=40, spacing=10)

            user_info = f"Name: {data['name'].title()} | Username: {username} | Role: {data['role'].title()}"
            user_label = Label(text=user_info, halign='left', valign='middle')

            delete_button = Button(text="Delete", size_hint=(None, 1), width=100)
            delete_button.bind(on_press=lambda instance, u=username: self.delete_user(u))

            user_box.add_widget(user_label)
            user_box.add_widget(delete_button)

            self.users_layout.add_widget(user_box)

    def delete_user(self, username):
        if username in USERS:
            del USERS[username]
            print(f"User '{username}' deleted.")
            self.load_users()  # Refresh the list

    def go_back(self, instance):
        self.manager.current = 'dashboard'
