
from kivy.metrics import dp
from kivymd.app import MDApp
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.uix.screenmanager import Screen
from kivy.properties import ObjectProperty
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.uix.dropdown import DropDown
from kivymd.uix.menu import MDDropdownMenu
from kivymd.uix.behaviors import BackgroundColorBehavior, \
    CommonElevationBehavior, RectangularRippleBehavior
from kivy.uix.behaviors import ButtonBehavior
import coordonnate  # importing the file containing the calcul coordonnee
import distance  # importing the file containing the calcul distance
import Menu
import cheng
import login

from step1 import Step1Form
from step2 import Step2Form

Window.clearcolor = 1, 1, 1, 1  # setting the window color
Window.size = (500, 700)  # setting the initial size of the window

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


class CustomButton(Button):
    ''''
    This class implements the graphics of a custom button specified in the custom_widgets.kv file
    '''
    pass


class OptionsDropdown(DropDown):
    ''''
    This class implements the graphics of a custom dropdown specified in the custom_widgets.kv file
    '''
    pass

    

class MainWidget(Widget):
    '''
    This class describes the main widget of the Home screen
    '''

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.menu = None

    def open_menu(self):
        app = MDApp.get_running_app()
        app.root.current = 'menu'


    # Showing dropdown menu of the toolbar
    def show_options(self):
        main_item = {"text": "Accueil",
                     "viewclass": "OneLineListItem",
                     "height": dp(40),
                     "on_release": lambda x="Settings": self.return_to_home(),
                     }
        settings_item = {"text": "Paramètre",
                         "viewclass": "OneLineListItem",
                         "height": dp(40),
                         "on_release": lambda x="Paramètre": self.button_callback(x),
                         }
        history_item = {"text": "Historiques",
                        "viewclass": "OneLineListItem",
                        "height": dp(40),
                        "on_release": lambda x="Historiques": self.button_callback(x),
                        }
        logout_item = {"text": "Déconnexion",
                       "viewclass": "OneLineListItem",
                       "height": dp(40),
                       "on_release": lambda x="Déconnexion": self.button_callback(x),
                       }
        exit_item = {"text": "Quitter",
                     "viewclass": "OneLineListItem",
                     "height": dp(40),
                     "on_release": lambda x="Quitter": self.button_callback(x),
                     }

        menu_items = [main_item, settings_item, history_item, logout_item, exit_item]
        self.menu = MDDropdownMenu(
            caller=self.ids.toolbar,
            items=menu_items,
            width_mult=3,
        )
        self.menu.open()

    # Go back to home method
    def return_to_home(self):
        app = MDApp.get_running_app()
        app.root.current = 'Accueil'
        self.menu.dismiss()

    # general method for buttons in the dropdown menu, to be replaced at need
    def button_callback(self, text_item):
        print(text_item)
        self.menu.dismiss()

    #this method is required by the toolbar
    def clear_fields(self):
        pass

class ArtiCalculatrice(MDApp):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # loading the screenmanager
        self.screens_manager = Builder.load_file('screen_manager.kv')

    def build(self):
        return self.screens_manager


    # Go to the previous screen
    def go_to_previous(self, root):
        root.clear_fields()
        if self.screens_manager.previous() != 'LoginPage':
            self.screens_manager.current = self.screens_manager.previous()
        else:
            # cannot go back to the login page
            self.screens_manager.current = self.screens_manager.previous()
            self.screens_manager.current = self.screens_manager.previous()


ArtiCalculatrice().run()

