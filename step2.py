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
    # def on_focus(self, instance, value):
    #     if value:
    #         print('User focused', instance)
    #         self.text = ''
    #         app = MDApp.get_running_app()
    #         self.foreground_color = app.theme_cls.primary_color
    #     else:
    #         print('User defocused', instance)


class Step2Form(BoxLayout):
    step = NumericProperty(2)
    pD1 = NumericProperty(0)
    pF1 = NumericProperty(0)
    pG1 = NumericProperty(0)


    def calculate_step2(self):
        # Récupérer les valeurs des champs de saisie
        self.p1D = float(self.ids.pD1.text)
        self.pF1 = float(self.ids.pF1.text)
        self.pG1 = float(self.ids.pG1.text)

        # Vérifier si les données de l'étape 1 sont présentes
        data_store = DataStore()

        BCrk = DataStore.BCrk
        Frk = DataStore.Frk

        # Effectuer le calcul
        BCx1 = round((-1) * self.pD1 /  ((-1) * self.pG1 ))
        Fx1 = round((-1) * self.pF1  + 0.01 * (-1) * self.pD1 )
        # print("BCx=\t=\t", format(BCx, ".0f"))
        # print("Fx=\t=\t", format(Fx, ".0f"))
        BCrc1 = BCrk + BCx1
        # print("BCrc=\t=\t", format(BCrc, ".0f"))
        Frc1 = Frk + Fx1

        # Stocker les données dans le DataStore
        DataStore.Frc1 = Frc1
        DataStore.BCrc1 = BCrc1
        DataStore.Fx1 = Fx1
        DataStore.BCx1 = BCx1
        # Afficher le résultat
        self.ids.result_BCx1.text = str(BCx1)
        self.ids.result_Fx1.text = str(Fx1)
        self.ids.result_BCrc1.text = str(BCrc1)
        self.ids.result_Frc1.text = str(Frc1)

        # Passer à l'étape suivante
        self.step = 3

    def clear_fields(self):
        self.pD1 = 0
        self.pF1 = 0
        self.pG1 = 0
        self.ids.result_BCx1.text = ''
        self.ids.result_Fx1.text = ''
        self.ids.result_BCrc1.text = ''
        self.ids.result_Frc1.text = ''