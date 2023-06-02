from kivymd.app import MDApp
from kivy.uix.screenmanager import Screen
from kivymd.uix.behaviors import BackgroundColorBehavior, \
    CommonElevationBehavior, RectangularRippleBehavior
from kivy.uix.behaviors import ButtonBehavior


class RectangularElevationButton(
    ButtonBehavior,
    RectangularRippleBehavior,
    CommonElevationBehavior,
    BackgroundColorBehavior,
):
    '''
    This class implements custom button with shadow
    '''
    pass

class LoginPage(Screen):
    

    def login(self,password):
        if self.check_password(password):
            app = MDApp.get_running_app()
            app.root.current = 'Accueil'
        else:
            self.ids.error_label.text = 'Incorrect password'
            self.ids.user_password.text = ''

    def check_password(self,password):
        # the method will return True if the password is correcte, False otherwise
        with open('password_storage.txt', 'r') as pwd_storage:
            pwd = pwd_storage.readline()
            if password == pwd:
                return True
            else:
                return False