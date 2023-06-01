from kivymd.app import MDApp
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.core.window import Window
import math
from kivymd.uix.button import MDFillRoundFlatButton
from kivymd.uix.behaviors import BackgroundColorBehavior, \
    CommonElevationBehavior, RectangularRippleBehavior
from kivymd.uix.menu import MDDropdownMenu
from kivy.metrics import dp
from kivy.uix.image import Image
from kivy.uix.behaviors import ButtonBehavior
from kivy.lang import Builder

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
    # def on_text(self, instance, value):
    #     if self.error == False:
    #         if len(self.text) >= 6:
    #             self.text = self.text[0:5]

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


class CoordonneeWidget(BoxLayout):
    '''
    This class describes the main widget of the calculator screen
    '''
    def check_aab_value(self):
        self.limit_data_input_range(self.ids.aab)

    # Limit data range of a text input
    def limit_data_input_range(self, widget):
        max_value = 6000
        try:
            if self.ids.degree_checkbox.active:
                max_value = 360
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
        self.ids.Xa.text = "0"
        self.ids.Ya.text = "0"
        self.ids.Ha.text = "0"
        self.ids.aab.text = "0"
        self.ids.Dab.text = "0"
        self.ids.e.text = "0"
        # self.ids.Xa.foreground_color = app.theme_cls.primary_color
        # self.ids.Ya.foreground_color = app.theme_cls.primary_color
        # self.ids.Ha.foreground_color = app.theme_cls.primary_color
        # self.ids.aab.foreground_color = app.theme_cls.primary_color
        # self.ids.Dab.foreground_color = app.theme_cls.primary_color
        # self.ids.e.foreground_color = app.theme_cls.primary_color
        self.ids.Xa.foreground_color = (0,0,0,1)
        self.ids.Ya.foreground_color = (0,0,0,1)
        self.ids.Ha.foreground_color = (0,0,0,1)
        self.ids.aab.foreground_color = (0,0,0,1)
        self.ids.Dab.foreground_color = (0,0,0,1)
        self.ids.e.foreground_color = (0,0,0,1)
        self.ids.result_Xb.text = ""
        self.ids.result_Yb.text = ""
        self.ids.result_Hb.text = ""


    # Algorithm to be used to compute results
    def perform_algorithm(self, option, Xa, Ya, Ha, aab, Dab, e ):

        if self.ids.degree_checkbox.active:
            if (option == "+"):
                A = Dab * math.cos((aab * math.pi) / 180)
                if Xa < 10000:
                    result1 = Xa + 100000 + A
                    Xb = format(result1, ".0f")
                else:
                    result1 = Xa + A
                    Xb = format(result1, ".0f")

                B = Dab * math.sin((aab * math.pi) / 180)
                if Ya < 10000:
                    result2 = Ya + 100000 + B
                    Yb = format(result2, ".0f")
                else:
                    result2 = Ya + B
                    Yb = format(result2, ".0f")
                result3 = Ha + Dab * math.tan((e * math.pi) / 180)
                Hb = format(result3, ".0f")
            return Xb, Yb, Hb
        else:
            if (option == "+"):
                A = Dab * math.cos((aab * math.pi) / 3000)
                if Xa < 10000:
                    result1 = Xa + 100000 + A
                    Xb = format(result1, ".0f")
                else:
                    result1 = Xa + A
                    Xb = format(result1, ".0f")

                B = Dab * math.sin((aab * math.pi) / 3000)
                if Ya < 10000:
                    result2 = Ya + 100000 + B
                    Yb = format(result2, ".0f")
                else:
                    result2 = Ya + B
                    Yb = format(result2, ".0f")
                result3 = Ha + Dab * math.tan((e * math.pi) / 3000)
                Hb = format(result3, ".0f")
        return Xb, Yb, Hb

    # Calculating results given the input data, handling input errors
    def validate(self, option):
        app = MDApp.get_running_app()
        # Ha is optional fields, therefore if the user does not insert any value or values different from digits are inserted, the default value 0 is set.
        if not self.ids.Ha.text.replace('.', '', 1).isdigit():
            self.ids.Ha.foreground_color = app.theme_cls.primary_color
            self.ids.Ha.text = '0'
        if not self.ids.e.text.replace('.', '', 1).isdigit():
            self.ids.e.foreground_color = app.theme_cls.primary_color
            self.ids.e.text = '0'

        try:
            Xa = float(self.ids.Xa.text)
            Ya = float(self.ids.Ya.text)
            Ha = float(self.ids.Ha.text)
            aab = float(self.ids.aab.text)
            Dab = float(self.ids.Dab.text)
            e = float(self.ids.e.text)
            Xb, Yb, Hb = self.perform_algorithm(option, Xa, Ya, Ha, aab, Dab, e)
            self.write_results(Xb, Yb, Hb)
        except:
            self.show_error_missing_input()
            print('Input error')

    # Showing 'missing data' message on the input fields that have no value during the validation method
    def show_error_missing_input(self):
        text = "Missing data"
        Xa = self.ids.Xa
        Ya = self.ids.Ya
        aab = self.ids.aab
        Dab = self.ids.Dab
        if self.ids.Xa.text == '':
            Xa.error = True
            Xa.foreground_color = (1, 0, 0, 1)
            Xa.text = text
        if self.ids.Ya.text == '':
            Ya.error = True
            Ya.foreground_color = (1, 0, 0, 1)
            Ya.text = text
        if self.ids.aab.text == '':
            aab.error = True
            aab.foreground_color = (1, 0, 0, 1)
            aab.text = text
        if self.ids.Dab.text == '':
            Dab.error = True
            Dab.foreground_color = (1, 0, 0, 1)
            Dab.text = text


    # Writing results calculated on the interface
    def write_results(self, Xb, Yb, Hb):
        self.ids.result_Xb.text = Xb
        self.ids.result_Yb.text = Yb
        self.ids.result_Hb.text = Hb

    # Go back to home screen
    def return_to_home(self):
        app = MDApp.get_running_app()
        app.root.current = 'Accueil'
        try:
            self.menu.dismiss()
        except:
            print('No menu to dismiss')
        self.clear_fields()
