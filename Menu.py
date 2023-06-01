from kivy.metrics import dp
from kivymd.app import MDApp
from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.lang import Builder
from kivy.core.window import Window
from kivymd.uix.menu import MDDropdownMenu
from kivymd.uix.behaviors import BackgroundColorBehavior, \
    CommonElevationBehavior, RectangularRippleBehavior
from kivy.uix.behaviors import ButtonBehavior



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



class Menu_Widget(BoxLayout):


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

        # Go the calculator screen

    def open_coordonnate(self):
        app = MDApp.get_running_app()
        app.root.current = 'coordonnate'

    def open_distance(self):
        app = MDApp.get_running_app()
        app.root.current = 'distance'

    def open_cheng(self):
        app = MDApp.get_running_app()
        app.root.current = 'cheng'

    # general method for buttons in the dropdown menu, to be replaced at need
    def button_callback(self, text_item):
        print(text_item)
        self.menu.dismiss()

# Go back to home screen
    def return_to_home(self):
        app = MDApp.get_running_app()
        app.root.current='Accueil'
        try:
            self.menu.dismiss()
        except:
            print('No menu to dismiss')

    # this method is required by the toolbar
    def clear_fields(self):
        pass
