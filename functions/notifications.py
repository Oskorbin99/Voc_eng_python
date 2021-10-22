# -----------------------------------------------------------
# Import classical and Pyqt5`s modules
# -----------------------------------------------------------
from PyQt5.QtWidgets import QMessageBox

# View QMessageBox about error
# (Example about failed sql request)
def view_error_critical(title, text):
    msg = QMessageBox()
    msg.setIcon(QMessageBox.Critical)
    msg.setWindowTitle(title)
    msg.setText(text)
    msg.exec_()

def view_info_transcription(text):
    msg = QMessageBox()
    msg.setIcon(QMessageBox.Information)
    msg.setWindowTitle("Дефиниция")
    msg.setText("Дефиниция:\n" + str(text))
    msg.exec_()