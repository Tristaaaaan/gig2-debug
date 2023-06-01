from kivymd.app import MDApp
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.core.window import Window
import math
from kivymd.uix.button import MDFillRoundFlatButton
from kivymd.uix.behaviors import BackgroundColorBehavior, CommonElevationBehavior, RectangularRippleBehavior
from kivymd.uix.menu import MDDropdownMenu
from kivy.metrics import dp
from kivy.properties import StringProperty
from kivy.uix.image import Image
from kivy.uix.behaviors import ButtonBehavior
from kivy.uix.popup import Popup


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


class DataInput(TextInput):
    '''
    This class implements methods of the custom widget DataInput, used to make the user able to insert input data.
    '''
    error = False  # flag used to indicate if there is an error with the input data
    multiline = False  # input cannot be on more than one line

    # allowing the user to use backspace to erase the input
    def keyboard_on_key_up(self, keycode, text):
        if text[0] == 'backspace':
            self.do_backspace()

    # During data inserting verifying that the number of characters does not exceed the maximum allowed
    def on_text(self, instance, value):
        if self.error == False:
            if len(self.text) >= 6:
                self.text = self.text[0:5]

    # When focused, erase the content of a text input automatically
    def on_focus(self, instance, value):
        if value:
            print('User focused', instance)
            self.text = ''
            app = MDApp.get_running_app()
            # self.foreground_color = app.theme_cls.primary_color
            self.foreground_color = (0,0,0,1)
        else:
            print('User defocused', instance)


class DistanceWidget(BoxLayout):


    '''
    This class describes the main widget of the calculator screen
    '''

    # Limit data range of a text input
    '''def limit_data_input_range(self, widget):
        try:
            # checking error condition
            if float(widget.text) > 3000 or float(widget.text) < 0:
                widget.focus = False
                widget.error = True
                widget.foreground_color = (1, 0, 0, 1)
                widget.text = "Max value 3000"
        except:
            pass'''
    
    def check_A_B_value(self):
        self.limit_data_input_range(self.ids.A)
        self.limit_data_input_range(self.ids.B)

    def limit_data_input_range(self, widget):
        max_value = 3000
        try:
            if self.ids.degree_checkbox.active:
                max_value = 180
            # checking error condition
            if float(widget.text) > max_value or float(widget.text) < 0:
                widget.focus = False
                widget.error = True
                widget.foreground_color = (1, 0, 0, 1)
                widget.text = f"Max value {max_value}"
        except:
            print('gere')

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

    # Resetting all text input to default values
    def clear_fields(self):
        app = MDApp.get_running_app()
        self.ids.Dab.text = "0"
        self.ids.A.text = "0"
        self.ids.B.text = "0"
        # self.ids.Dab.foreground_color = app.theme_cls.primary_color
        # self.ids.A.foreground_color = app.theme_cls.primary_color
        # self.ids.B.foreground_color = app.theme_cls.primary_color
        self.ids.Dab.foreground_color = (0,0,0,1)
        self.ids.A.foreground_color = (0,0,0,1)
        self.ids.B.foreground_color = (0,0,0,1)
        self.ids.result_Dac.text = ""
        self.ids.result_Dbc.text = ""


        # Algorithm to be used to compute results
    def perform_algorithm(self,option, Dab, A, B ):
        if self.ids.degree_checkbox.active:
            if (option == "+"):
                C = 360 - int(A + B)
                Dac = (math.sin((B * math.pi) / 180) * Dab) / (
                    math.sin((C * math.pi / 180)))
                Dac = format(Dac, ".0f")
                Dbc = math.sin((A * math.pi) / 180) * Dab / (
                    math.sin((C * math.pi / 180)))
                Dbc = format(Dbc, ".0f")
        else:
            if (option == "+"):
                C = 3000 - int(A + B)
                Dac = (math.sin((B * math.pi) / 3000) * Dab) / (
                    math.sin((C * math.pi / 3000)))
                Dac = format(Dac, ".0f")
                Dbc = math.sin((A * math.pi) / 3000) * Dab / (
                    math.sin((C * math.pi / 3000)))
                Dbc = format(Dbc, ".0f")
        return Dac, Dbc, C


    # Calculating results given the input data, handling input errors
    def validate(self, option):
        app = MDApp.get_running_app()
        # Ha is optional fields, therefore if the user does not insert any value or values different from digits are inserted, the default value 0 is set.

        Dab = float(self.ids.Dab.text)
        A = float(self.ids.A.text)
        B = float(self.ids.B.text)

        Dac, Dbc, C = self.perform_algorithm(option, Dab, A, B)
        self.write_results(Dac, Dbc, C)

    # Showing 'missing data' message on the input fields that have no value during the validation method
    def show_error_missing_input(self):
        text = "Missing data"
        Dab = self.ids.Dab
        A = self.ids.A
        B = self.ids.B

        if self.ids.Xa.text == '':
            Dab.error = True
            Dab.foreground_color = (1, 0, 0, 1)
            Dab.text = text
        if self.ids.A.text == '':
            A.error = True
            A.foreground_color = (1, 0, 0, 1)
            A.text = text
        if self.ids.B.text == '':
            B.error = True
            B.foreground_color = (1, 0, 0, 1)
            B.text = text

    # Writing results calculated on the interface
    def write_results(self, Dac, Dbc, C):
        self.ids.result_Dac.text = Dac
        self.ids.result_Dbc.text = Dbc
        self.C = str(C)



    # Go back to home screen
    def return_to_home(self):
        app = MDApp.get_running_app()
        app.root.current = 'Accueil'
        try:
            self.menu.dismiss()
        except:
            print('No menu to dismiss')
        self.clear_fields()


