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
        app = MDApp.get_running_app()
        with open('password_storage.txt', 'r') as pwd_storage:
            pwd = tuple(pwd_storage.readline().split(','))
            if self.check_password(pwd[0],password):
                app.root.current = 'Accueil'
            else:
                self.ids.error_label.text = 'Incorrect password'
                self.ids.user_password.text = ''

    def check_password(self,pwd,password):
        # the method will return True if the password is correcte, False otherwise
            if password == pwd:
                with open('password_storage.txt', 'w') as pwd_storage:
                    pwd_storage.write(f'{pwd},1')
                    return True
            else:
                return False