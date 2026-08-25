from PySide6.QtWidgets import QWidget
from ui_adminpage import Ui_Form   # اصلاح شد

class AdminPage(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Form()
        self.ui.setupUi(self)
