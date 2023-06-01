from kivymd.app import MDApp
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.properties import NumericProperty
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
from kivy.lang import Builder
import math
from kivymd.uix.button import MDFillRoundFlatButton
from kivymd.uix.behaviors import BackgroundColorBehavior, CommonElevationBehavior, RectangularRippleBehavior
from kivymd.uix.menu import MDDropdownMenu
from kivy.metrics import dp
from kivy.uix.image import Image
from kivy.uix.behaviors import ButtonBehavior
from datastore import DataStore


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

    def __init__(self, **kwargs):
        super(DataInput, self).__init__(**kwargs)
        self.default_text = "0"  # Default text to be replaced
    # allowing the user to use backspace to erase the input
    
    def keyboard_on_key_up(self, keycode, text):
        if text[0] == 'backspace':
            self.do_backspace()

    # During data inserting verifying that the number of characters does not exceed the maximum allowed
    def on_text(self, instance, value):
        # if self.error == False:
        #     if len(self.text) >= 6:
        #         self.text = self.text[0:5]
        pass

    # When focused, erase the content of a text input automatically
    def on_focus(self, instance, value):
        if value:
            print('User focused', instance)
            self.text = ''
            app = MDApp.get_running_app()
            self.foreground_color = app.theme_cls.primary_color
        else:
            print('User defocused', instance)


class Step1Form(BoxLayout):
    step = NumericProperty(1)
    pD = NumericProperty(0)
    pF = NumericProperty(0)
    pG = NumericProperty(0)

    def calculate_step1(self):
        # Récupérer les valeurs des champs de saisie
        self.pD = float(self.ids.pD.text)
        self.pF = float(self.ids.pF.text)
        self.pG = float(self.ids.pG.text)

        # Effectuer le calcul
        BCrk = round((-1) * self.pD / 2)
        Frk = round((-1) * self.pF * self.pG)


        # Stocker les données dans le DataStore
        DataStore.Frk= Frk
        DataStore.BCrck = BCrk

        # Afficher le résultat

        self.ids.result_BCrk.text = str(BCrk)
        self.ids.result_Frk.text = str(Frk)

        # Passer à l'étape suivante
        self.step = 2

    def clear_fields(self):
        self.pD = 0
        self.pF = 0
        self.pG = 0
        self.ids.result_BCrk.text = ''
        self.ids.result_Frk.text = ''
