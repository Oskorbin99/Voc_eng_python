# -----------------------------------------------------------
# Import classical and Pyqt5`s modules
# -----------------------------------------------------------
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QLabel
from PyQt5 import QtCore
# -----------------------------------------------------------
# Codes other files project
# -----------------------------------------------------------
from database.work_data_bd import WorkDataBd
from functions.main_buttons import MainButtons

import settings
# -----------------------------------------------------------
# Import other modules
# -----------------------------------------------------------

# Class to describe  main labels
class MainLabels(WorkDataBd):

    # create labels
    def name_labels(self):
        self.time = QtCore.QTime(0, 0, 0)
        self.text_labels = [
            'Время: 00:00:00',
            'Всего слов: ',
            'Непроверенные слова: ',
            'Проверенные слова: ',
            'Старые слова: ',
            'Количество очков слова: ',
            'Часть слова: ',
            'Перевод слова: ',
            'Транскрипция: ',
            'Тема: ',
            '*********************************************',
            # id -- 11. Word "Неправильно"
            "Неправильно",
            # id -- 12. Entered word
            "Неправильный вариант: ",
            # id -- 13. True translate
            "Правильный вариант: ",
            # id -- 14. Transcription
            "Транскрипция: ",
        ]
        self.information_labels = {
            "timer learn": QLabel(),
            "sum words learn": QLabel(),
            "false words": QLabel(),
            "true words": QLabel(),
            "change words learn": QLabel(),
            "count word now": QLabel(),
            "parts of speech word now": QLabel(),
            "word now": QLabel(),
            "transcription word now": QLabel(),
            "chapter word now": QLabel(),
            "line between bd and word": QLabel(),
            # above text edit
            "status word": QLabel(),
            "wrong one": QLabel(),
            "right one": QLabel(),
            "transcription word previous": QLabel(),

        }
        self.timer()

    # describe font and size labels text
    def label_set_font_and_size(self):
        size_label_font = 15
        name_label_font = 'Arial'
        for element in self.information_labels:
            self.information_labels[element].setFont(QFont(name_label_font, size_label_font))

    # change word
    def label_set_text(self, random_id=1, language="ru"):
        lang_now = MainButtons.check_language_word(MainButtons, language)
        if random_id != -1:
            self.list_now_word = self.get_row(random_id)
        else:
            self.list_now_word = ["", "", "", "", "", "", "", "", ""]
        self.information_labels["sum words learn"]. \
            setText(self.text_labels[1] + str(self.get_count_all_word()[0]))
        self.information_labels["false words"]. \
            setText(self.text_labels[2] + str(self.get_count_false_world()[0]))
        self.information_labels["true words"]. \
            setText(self.text_labels[3] + str(self.get_count_true_world()[0]))
        self.information_labels["change words learn"]. \
            setText(self.text_labels[4] + str(self.get_count_change_world()[0]))
        self.information_labels["count word now"]. \
            setText(self.text_labels[5] + str(self.list_now_word[8]))
        self.information_labels["parts of speech word now"]. \
            setText(self.text_labels[6] + self.list_now_word[3])

        self.information_labels["word now"]. \
            setText(self.text_labels[7] + self.list_now_word[lang_now])
        if language == "en":
            self.information_labels["transcription word now"]. \
                setText(self.text_labels[8] + str(self.list_now_word[4]))
        elif language == "ru":
            self.information_labels["transcription word now"]. \
                setText(self.text_labels[8] + " - ")
        self.information_labels["chapter word now"]. \
            setText(self.text_labels[9] + self.list_now_word[7])
        self.information_labels["line between bd and word"]. \
            setText(self.text_labels[10])

    # check enter word
    def wrong_enter_word(self, random_id_now, status_word="True", text_check=""):
        list_now_word = self.get_row(random_id_now)
        # if enter word is false
        if not status_word:
            # -----------------------------------------------------------
            # Output information about true translate now word
            # -----------------------------------------------------------
            index_check_word = 11
            self.information_labels["status word"].setText(
                f"{self.text_labels[index_check_word]}")
            self.information_labels["wrong one"].setText(
                f"{self.text_labels[index_check_word+1]}"
                f" {text_check[0:1].upper()}{text_check[1:].lower()}")
            self.information_labels["right one"].setText(
                f"{self.text_labels[index_check_word+2]}"
                f" {list_now_word[1]}"
                f" ="
                f" {list_now_word[2]}")
            self.information_labels["transcription word previous"].setText(
                f"{self.text_labels[index_check_word + 3]}"
                f" [ {list_now_word[4]} ]")
            # -----------------------------------------------------------
            # add 1 life to now word
            if list_now_word[8] < 3:
                self.edit_work_count_life(random_id_now, list_now_word[8] + 1)

        # if enter word is true
        else:
            # output information that translate now word is true
            self.information_labels["status word"].setText("Правильно")
            # -----------------------------------------------------------
            # clear information about last word
            self.information_labels["transcription word previous"].setText("")
            self.information_labels["wrong one"].setText("")
            self.information_labels["right one"].setText("")
            # -----------------------------------------------------------
            # add 1 life to now word
            if list_now_word[8] > 0:
                self.edit_work_count_life(random_id_now, list_now_word[8]-1)

    # Create timer
    def timer(self):
        self.timer_learn_1 = QtCore.QTimer(self)
        self.timer_learn_1.setInterval(1000)
        self.timer_learn_1.timeout.connect(self.timer_text)
        self.timer_learn_1.start()
        settings.TIMER_INTERVAL = 0

    # Change time to timer
    def timer_text(self):
        self.time = self.time.addSecs(settings.TIMER_INTERVAL)
        self.information_labels["timer learn"].setText(self.time.toString("Время: hh:mm:ss"))


    # Main label def
    def main_label_def(self):
        self.add_work_count_life()
        self.order_main_table()
        self.check_life_word()
        self.random_language_now = MainButtons.choice_ru_or_en_word(MainButtons)
        self.name_labels()
        self.label_set_font_and_size()
        self.label_set_text(self.random_id_now, self.random_language_now)
