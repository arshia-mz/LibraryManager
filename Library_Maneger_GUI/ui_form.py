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
from PySide6.QtWidgets import (QApplication, QGridLayout, QHBoxLayout, QLabel,
    QPushButton, QSizePolicy, QSpacerItem, QWidget)

class Ui_Widget(object):
    def setupUi(self, Widget):
        if not Widget.objectName():
            Widget.setObjectName(u"Widget")
        Widget.resize(1297, 813)
        Widget.setStyleSheet(u"background-color: #0f0f1a;\n"
"    color: #f1f5f9;\n"
"    font-family: Vazir, IRANSans, Tahoma;")
        self.gridLayout = QGridLayout(Widget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.horizontalSpacer_2 = QSpacerItem(100, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_2, 1, 2, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.gridLayout.addItem(self.verticalSpacer, 0, 1, 1, 1)

        self.verticalSpacer_2 = QSpacerItem(100, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.gridLayout.addItem(self.verticalSpacer_2, 2, 1, 1, 1)

        self.horizontalSpacer = QSpacerItem(100, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer, 1, 0, 1, 1)

        self.widget = QWidget(Widget)
        self.widget.setObjectName(u"widget")
        self.widget.setStyleSheet(u"background-color: #1e1e2e;\n"
"    border-radius: 12px;\n"
"    border: 1px solid #2d2d44;")
        self.label = QLabel(self.widget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(390, 10, 261, 81))
        font = QFont()
        font.setFamilies([u"Vazir"])
        font.setPointSize(20)
        self.label.setFont(font)
        self.label.setStyleSheet(u"border:none;\n"
"background:none;")
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.widget_2 = QWidget(self.widget)
        self.widget_2.setObjectName(u"widget_2")
        self.widget_2.setGeometry(QRect(280, 150, 501, 81))
        self.widget_2.setStyleSheet(u"border: 1px solid #2d2d44;\n"
"background-color: #161625;\n"
"")
        self.horizontalLayout = QHBoxLayout(self.widget_2)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.UserButton = QPushButton(self.widget_2)
        self.UserButton.setObjectName(u"UserButton")
        font1 = QFont()
        font1.setFamilies([u"Vazir"])
        self.UserButton.setFont(font1)
        self.UserButton.setStyleSheet(u"QPushButton {\n"
"    background-color: #161625;\n"
"    color: #94a3b8;\n"
"    border:none;\n"
"    border-radius: 8px;\n"
"    padding: 10px 30px;\n"
"    font-size: 20px;\n"
"	height:100%;\n"
"}\n"
"\n"
"QPushButton:checked {\n"
"    background-color: #3b82f6;\n"
"    color: white;\n"
"    border: 1px solid #3b82f6;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #1e1e2e;\n"
"}")

        self.horizontalLayout.addWidget(self.UserButton)

        self.AdminButton = QPushButton(self.widget_2)
        self.AdminButton.setObjectName(u"AdminButton")
        self.AdminButton.setFont(font1)
        self.AdminButton.setStyleSheet(u"QPushButton {\n"
"    background-color: #161625;\n"
"    color: #94a3b8;\n"
"    border: none;\n"
"    border-radius: 8px;\n"
"    padding: 10px 30px;\n"
"    font-size: 20px;\n"
"	height:100%;\n"
"}\n"
"\n"
"QPushButton:checked {\n"
"    background-color: #3b82f6;\n"
"    color: white;\n"
"    border: 1px solid #3b82f6;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #1e1e2e;\n"
"}")

        self.horizontalLayout.addWidget(self.AdminButton)


        self.gridLayout.addWidget(self.widget, 1, 1, 1, 1)


        self.retranslateUi(Widget)

        QMetaObject.connectSlotsByName(Widget)
    # setupUi

    def retranslateUi(self, Widget):
        Widget.setWindowTitle(QCoreApplication.translate("Widget", u"Widget", None))
        self.label.setText(QCoreApplication.translate("Widget", u"\u0645\u062f\u06cc\u0631\u06cc\u062a \u06a9\u062a\u0627\u0628\u062e\u0627\u0646\u0647", None))
        self.UserButton.setText(QCoreApplication.translate("Widget", u"\u06a9\u0627\u0631\u0628\u0631", None))
        self.AdminButton.setText(QCoreApplication.translate("Widget", u"\u0627\u062f\u0645\u06cc\u0646", None))
    # retranslateUi

