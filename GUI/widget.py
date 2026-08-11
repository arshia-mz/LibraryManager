# This Python file uses the following encoding: utf-8
import sys

from PySide6.QtWidgets import QApplication, QWidget

# Important:
# You need to run the following command to generate the ui_form.py file
#     pyside6-uic form.ui -o ui_form.py, or
#     pyside2-uic form.ui -o ui_form.py
from ui_form import Ui_Widget

class Widget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Widget()
        self.ui.setupUi(self)
        self.ui.Admin_Button.setCheckable(True)
        self.ui.User_Buttom.setCheckable(True)

        self.ui.Admin_Button.setChecked(True)
        if self.ui.Admin_Button.isChecked:
            self.ui.User_Login.hide()
            self.ui.User_Buttom.setChecked(False)
        



if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = Widget()
    widget.show()
    sys.exit(app.exec())
