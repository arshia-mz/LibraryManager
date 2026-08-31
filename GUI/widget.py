# This Python file uses the following encoding: utf-8
import sys

from PySide6.QtWidgets import QApplication, QWidget
from admin_page import AdminPage
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
        self.ui.Admin_Button.clicked.connect(self.AdminClick)
        self.ui.User_Buttom.clicked.connect(self.UserClick)

        self.ui.Login.clicked.connect(self.AdminLogged)


    def AdminClick(self):
        self.ui.Admin_Button.setChecked(True)
        self.ui.User_Buttom.setChecked(False)

    def UserClick(self):
        self.ui.Admin_Button.setChecked(False)
        self.ui.User_Buttom.setChecked(True)

    def AdminLogged(self):
        self.admin_page = AdminPage()
        self.admin_page.show()    



if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = Widget()
    widget.show()
    sys.exit(app.exec())
