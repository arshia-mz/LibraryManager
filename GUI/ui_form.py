# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 6.11.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QGroupBox,
    QHBoxLayout, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QSpacerItem, QVBoxLayout, QWidget)

class Ui_Widget(object):
    def setupUi(self, Widget):
        if not Widget.objectName():
            Widget.setObjectName(u"Widget")
        Widget.resize(1096, 839)
        Widget.setStyleSheet(u"QWidget {\n"
"    background-color: #0f0f1a;\n"
"    color: #f1f5f9;\n"
"    font-family: Vazir, IRANSans, Tahoma;\n"
"}")
        self.gridLayout = QGridLayout(Widget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.frame = QFrame(Widget)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"QFrame {\n"
"    background-color: #1e1e2e;\n"
"    border-radius: 12px;\n"
"    border: 1px solid #2d2d44;\n"
"}")
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_4 = QGridLayout(self.frame)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setFamilies([u"Vazir FD-WOL"])
        font.setPointSize(30)
        font.setBold(False)
        font.setItalic(False)
        self.label.setFont(font)
        self.label.setStyleSheet(u"background:none;\n"
"border:none;\n"
"font: 30pt \"Vazir FD-WOL\";")
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_4.addWidget(self.label, 0, 0, 1, 1)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.User_Login = QGroupBox(self.frame)
        self.User_Login.setObjectName(u"User_Login")
        self.User_Login.setStyleSheet(u"background:none;\n"
"border:none;")
        self.gridLayout_3 = QGridLayout(self.User_Login)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.gridLayout_3.addItem(self.verticalSpacer_4, 2, 1, 1, 1)

        self.horizontalSpacer_6 = QSpacerItem(100, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.gridLayout_3.addItem(self.horizontalSpacer_6, 1, 2, 1, 1)

        self.horizontalSpacer_5 = QSpacerItem(100, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.gridLayout_3.addItem(self.horizontalSpacer_5, 1, 0, 1, 1)

        self.pushButton = QPushButton(self.User_Login)
        self.pushButton.setObjectName(u"pushButton")
        font1 = QFont()
        font1.setFamilies([u"Vazir"])
        font1.setPointSize(18)
        self.pushButton.setFont(font1)
        self.pushButton.setStyleSheet(u"QPushButton {\n"
"    background-color: #3b82f6;\n"
"    color: white;\n"
"    border: none;\n"
"    border-radius: 10px;\n"
"    padding: 10px;\n"
"\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #2563eb;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #1d4ed8;\n"
"}")

        self.gridLayout_3.addWidget(self.pushButton, 1, 1, 1, 1)

        self.widget_2 = QWidget(self.User_Login)
        self.widget_2.setObjectName(u"widget_2")
        self.widget_2.setStyleSheet(u"background-color: none;\n"
"border:none;")
        self.verticalLayout_2 = QVBoxLayout(self.widget_2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.UserName_2 = QLineEdit(self.widget_2)
        self.UserName_2.setObjectName(u"UserName_2")
        self.UserName_2.setStyleSheet(u"QLineEdit {\n"
"    background-color: #161625;\n"
"    border: 1px solid #2d2d44;\n"
"    border-radius: 8px;\n"
"    padding: 10px;\n"
"    color: #f1f5f9;\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"    border: 1px solid #3b82f6;\n"
"}")
        self.UserName_2.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.verticalLayout_2.addWidget(self.UserName_2)

        self.Password_2 = QLineEdit(self.widget_2)
        self.Password_2.setObjectName(u"Password_2")
        self.Password_2.setStyleSheet(u"QLineEdit {\n"
"    background-color: #161625;\n"
"    border: 1px solid #2d2d44;\n"
"    border-radius: 8px;\n"
"    padding: 10px;\n"
"    color: #f1f5f9;\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"    border: 1px solid #3b82f6;\n"
"}")

        self.verticalLayout_2.addWidget(self.Password_2)


        self.gridLayout_3.addWidget(self.widget_2, 0, 0, 1, 3)


        self.verticalLayout_3.addWidget(self.User_Login)

        self.Admin_Login = QGroupBox(self.frame)
        self.Admin_Login.setObjectName(u"Admin_Login")
        self.Admin_Login.setStyleSheet(u"background:none;\n"
"border:none;")
        self.gridLayout_2 = QGridLayout(self.Admin_Login)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.horizontalSpacer_3 = QSpacerItem(100, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_3, 1, 0, 1, 1)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.gridLayout_2.addItem(self.verticalSpacer_3, 2, 1, 1, 1)

        self.Login = QPushButton(self.Admin_Login)
        self.Login.setObjectName(u"Login")
        font2 = QFont()
        font2.setFamilies([u"Vazir"])
        font2.setPointSize(18)
        font2.setBold(False)
        self.Login.setFont(font2)
        self.Login.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.Login.setStyleSheet(u"QPushButton {\n"
"    background-color: #3b82f6;\n"
"    color: white;\n"
"    border: none;\n"
"    border-radius: 10px;\n"
"    padding: 10px;\n"
"\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #2563eb;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #1d4ed8;\n"
"}")

        self.gridLayout_2.addWidget(self.Login, 1, 1, 1, 1)

        self.horizontalSpacer_4 = QSpacerItem(100, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_4, 1, 2, 1, 1)

        self.widget = QWidget(self.Admin_Login)
        self.widget.setObjectName(u"widget")
        self.widget.setStyleSheet(u"background-color: none;\n"
"border:none;")
        self.verticalLayout = QVBoxLayout(self.widget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.UserName = QLineEdit(self.widget)
        self.UserName.setObjectName(u"UserName")
        self.UserName.setStyleSheet(u"QLineEdit {\n"
"    background-color: #161625;\n"
"    border: 1px solid #2d2d44;\n"
"    border-radius: 8px;\n"
"    padding: 10px;\n"
"    color: #f1f5f9;\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"    border: 1px solid #3b82f6;\n"
"}")
        self.UserName.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.verticalLayout.addWidget(self.UserName)

        self.Password = QLineEdit(self.widget)
        self.Password.setObjectName(u"Password")
        self.Password.setStyleSheet(u"QLineEdit {\n"
"    background-color: #161625;\n"
"    border: 1px solid #2d2d44;\n"
"    border-radius: 8px;\n"
"    padding: 10px;\n"
"    color: #f1f5f9;\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"    border: 1px solid #3b82f6;\n"
"}")

        self.verticalLayout.addWidget(self.Password)


        self.gridLayout_2.addWidget(self.widget, 0, 0, 1, 3)


        self.verticalLayout_3.addWidget(self.Admin_Login)


        self.gridLayout_4.addLayout(self.verticalLayout_3, 2, 0, 1, 1)

        self.frame_2 = QFrame(self.frame)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_2)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.User_Buttom = QPushButton(self.frame_2)
        self.User_Buttom.setObjectName(u"User_Buttom")
        self.User_Buttom.setStyleSheet(u"QPushButton {\n"
"                background-color: #161625;\n"
"                color: #94a3b8;\n"
"                 border: none;\n"
"                border-radius: 8px;\n"
"                padding: 10px 30px;\n"
"                font-size: 14px;\n"
"                min-width: 120px;\n"
"            }\n"
"            QPushButton:checked {\n"
"                background-color: #3b82f6;\n"
"                color: white;\n"
"                border: none;\n"
"            }\n"
"            QPushButton:hover {\n"
"                background-color: #1e1e2e;\n"
"            }")

        self.horizontalLayout.addWidget(self.User_Buttom)

        self.Admin_Button = QPushButton(self.frame_2)
        self.Admin_Button.setObjectName(u"Admin_Button")
        self.Admin_Button.setStyleSheet(u"QPushButton {\n"
"                background-color: #161625;\n"
"                color: #94a3b8;\n"
"                 border: none;\n"
"                border-radius: 8px;\n"
"                padding: 10px 30px;\n"
"                font-size: 14px;\n"
"                min-width: 120px;\n"
"            }\n"
"            QPushButton:checked {\n"
"                background-color: #3b82f6;\n"
"                color: white;\n"
"                 border: none;\n"
"            }\n"
"            QPushButton:hover {\n"
"                background-color: #1e1e2e;\n"
"            }")

        self.horizontalLayout.addWidget(self.Admin_Button)


        self.gridLayout_4.addWidget(self.frame_2, 1, 0, 1, 1)


        self.gridLayout.addWidget(self.frame, 1, 1, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(100, 100, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_2, 1, 2, 1, 1)

        self.verticalSpacer_2 = QSpacerItem(20, 100, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.gridLayout.addItem(self.verticalSpacer_2, 2, 1, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 100, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.gridLayout.addItem(self.verticalSpacer, 0, 1, 1, 1)

        self.horizontalSpacer = QSpacerItem(100, 100, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer, 1, 0, 1, 1)


        self.retranslateUi(Widget)

        QMetaObject.connectSlotsByName(Widget)
    # setupUi

    def retranslateUi(self, Widget):
        Widget.setWindowTitle(QCoreApplication.translate("Widget", u"Widget", None))
        self.label.setText(QCoreApplication.translate("Widget", u"\u0645\u062f\u06cc\u0631\u06cc\u062a \u06a9\u062a\u0627\u0628\u062e\u0627\u0646\u0647", None))
        self.User_Login.setTitle("")
        self.pushButton.setText(QCoreApplication.translate("Widget", u"\u0648\u0631\u0648\u062f", None))
        self.UserName_2.setPlaceholderText(QCoreApplication.translate("Widget", u"\u0646\u0627\u0645 \u06a9\u0627\u0631\u0628\u0631\u06cc", None))
        self.Password_2.setPlaceholderText(QCoreApplication.translate("Widget", u"\u0631\u0645\u0632 \u0639\u0628\u0648\u0631", None))
        self.Admin_Login.setTitle("")
        self.Login.setText(QCoreApplication.translate("Widget", u"\u0648\u0631\u0648\u062f", None))
        self.UserName.setPlaceholderText(QCoreApplication.translate("Widget", u"\u0646\u0627\u0645 \u06a9\u0627\u0631\u0628\u0631\u06cc", None))
        self.Password.setPlaceholderText(QCoreApplication.translate("Widget", u"\u0631\u0645\u0632 \u0639\u0628\u0648\u0631", None))
        self.User_Buttom.setText(QCoreApplication.translate("Widget", u"\u06a9\u0627\u0631\u0628\u0631", None))
        self.Admin_Button.setText(QCoreApplication.translate("Widget", u"\u0627\u062f\u0645\u06cc\u0646", None))
    # retranslateUi

