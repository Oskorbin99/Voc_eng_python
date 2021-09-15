# -----------------------------------------------------------
# Import classical and Pyqt5`s modules
# -----------------------------------------------------------
from PyQt5.QtWidgets import QPushButton
import random

# -----------------------------------------------------------
# Codes other files project
# -----------------------------------------------------------
from settings import LANGUAGE


# Class to describe  main buttons
class Main_buttons:

    # def to create main_button
    def create_main_button(self):
        self.btn = QPushButton('Проверить', self)
        self.btn.setStyleSheet("QPushButton"
                               "{"
                               "background-color : lightblue;"
                               "}"
                               "QPushButton::pressed"
                               "{"
                               "background-color : gray;"
                               "}"
                               )

    def choice_ru_or_en_word(self):
        return random.choice(LANGUAGE)