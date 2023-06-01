from kivymd.app import MDApp
from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.uix.dropdown import DropDown
from kivymd.uix.menu import MDDropdownMenu
from kivy.uix.button import Button
from step1 import Step1Form
from step2 import Step2Form
from kivy.properties import NumericProperty, ObjectProperty
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.metrics import dp


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

class DataInput:
    pass


class MainScreen(Screen):
    data_store = ObjectProperty(None)

    # def change_screen(self, step):
    #     screen_manager = self.ids.screen_manager
    #     screen_name = "step" + str(step)
    #     screen_manager.current = screen_name

    def switch_view(self, view_name):
        # screen_manager = self.root.ids.screen_manager
        self.ids.screen_manager.current = view_name
    
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

    # general method for buttons in the dropdown menu, to be replaced at need
    def button_callback(self, text_item):
        print(text_item)
        self.menu.dismiss()
    
    # Go back to home screen
    def return_to_home(self):
        app = MDApp.get_running_app()
        self.clear_fields()
        app.root.current = 'Accueil'
        try:
            self.menu.dismiss()
        except:
            print('No menu to dismiss')


    def clear_fields(self):
        screen1 = self.ids.screen_manager.screens[0]
        screen2 = self.ids.screen_manager.screens[1]
        screen1.children[1].clear_fields()
        screen2.children[1].clear_fields()
