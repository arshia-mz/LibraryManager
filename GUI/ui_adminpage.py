# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'adminpage.ui'
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QHBoxLayout, QHeaderView,
    QLabel, QPushButton, QSizePolicy, QSpacerItem,
    QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(1071, 800)
        Form.setStyleSheet(u"background-color:#0f0f1a;\n"
"\n"
"")
        self.horizontalLayout_3 = QHBoxLayout(Form)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.menuBar = QWidget(Form)
        self.menuBar.setObjectName(u"menuBar")
        self.menuBar.setStyleSheet(u"#menuBar{\n"
"background-color:#161625;\n"
"width:40%;\n"
"}\n"
"\n"
"#menuBar QPushButton{\n"
"	font-family:\"Yekan Bakh\";\n"
"	font-size:20px;\n"
"	font-weight:500;\n"
"	background-color:#3b82f6;\n"
"	padding:10px;\n"
"	border-radius:10px;\n"
"	color:#fff;\n"
"	width:100%;\n"
"	margin:10px;\n"
"}\n"
"#menuBar QPushButton:hover{\n"
"	\n"
"	background-color: rgb(37, 99, 235);\n"
"}")
        self.verticalLayout_2 = QVBoxLayout(self.menuBar)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.pushButton = QPushButton(self.menuBar)
        self.pushButton.setObjectName(u"pushButton")

        self.verticalLayout.addWidget(self.pushButton)

        self.pushButton_2 = QPushButton(self.menuBar)
        self.pushButton_2.setObjectName(u"pushButton_2")

        self.verticalLayout.addWidget(self.pushButton_2)

        self.pushButton_3 = QPushButton(self.menuBar)
        self.pushButton_3.setObjectName(u"pushButton_3")

        self.verticalLayout.addWidget(self.pushButton_3)

        self.pushButton_4 = QPushButton(self.menuBar)
        self.pushButton_4.setObjectName(u"pushButton_4")

        self.verticalLayout.addWidget(self.pushButton_4)

        self.pushButton_5 = QPushButton(self.menuBar)
        self.pushButton_5.setObjectName(u"pushButton_5")

        self.verticalLayout.addWidget(self.pushButton_5)

        self.pushButton_6 = QPushButton(self.menuBar)
        self.pushButton_6.setObjectName(u"pushButton_6")

        self.verticalLayout.addWidget(self.pushButton_6)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.pushButton_7 = QPushButton(self.menuBar)
        self.pushButton_7.setObjectName(u"pushButton_7")

        self.verticalLayout.addWidget(self.pushButton_7)


        self.verticalLayout_2.addLayout(self.verticalLayout)


        self.horizontalLayout_2.addWidget(self.menuBar)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.widget = QWidget(Form)
        self.widget.setObjectName(u"widget")
        self.horizontalLayout = QHBoxLayout(self.widget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.Title = QLabel(self.widget)
        self.Title.setObjectName(u"Title")
        font = QFont()
        font.setFamilies([u"Yekan Bakh"])
        font.setPointSize(20)
        self.Title.setFont(font)

        self.horizontalLayout.addWidget(self.Title)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.Admi_Name = QLabel(self.widget)
        self.Admi_Name.setObjectName(u"Admi_Name")
        self.Admi_Name.setFont(font)

        self.horizontalLayout.addWidget(self.Admi_Name)


        self.verticalLayout_3.addWidget(self.widget)

        self.widget_2 = QWidget(Form)
        self.widget_2.setObjectName(u"widget_2")
        self.widget_2.setStyleSheet(u"width:60%;")
        self.gridLayout = QGridLayout(self.widget_2)
        self.gridLayout.setObjectName(u"gridLayout")
        self.tableWidget = QTableWidget(self.widget_2)
        self.tableWidget.setObjectName(u"tableWidget")

        self.gridLayout.addWidget(self.tableWidget, 0, 0, 1, 1)


        self.verticalLayout_3.addWidget(self.widget_2)


        self.horizontalLayout_2.addLayout(self.verticalLayout_3)


        self.horizontalLayout_3.addLayout(self.horizontalLayout_2)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.pushButton.setText(QCoreApplication.translate("Form", u"\u0627\u0641\u0632\u0648\u062f\u0646 \u06a9\u062a\u0627\u0628", None))
        self.pushButton_2.setText(QCoreApplication.translate("Form", u"\u062d\u0630\u0641 \u06a9\u062a\u0627\u0628", None))
        self.pushButton_3.setText(QCoreApplication.translate("Form", u"\u0627\u0645\u0627\u0646\u062a \u062f\u0627\u062f\u0646", None))
        self.pushButton_4.setText(QCoreApplication.translate("Form", u"\u0628\u0631\u06af\u0634\u062a \u06a9\u062a\u0627\u0628", None))
        self.pushButton_5.setText(QCoreApplication.translate("Form", u"\u0646\u0645\u0627\u06cc\u0634 \u0647\u0645\u0647", None))
        self.pushButton_6.setText(QCoreApplication.translate("Form", u"\u062c\u0633\u062a \u0648 \u062c\u0648", None))
        self.pushButton_7.setText(QCoreApplication.translate("Form", u"\u062e\u0631\u0648\u062c", None))
        self.Title.setText(QCoreApplication.translate("Form", u"\u067e\u0646\u0644 \u0645\u062f\u06cc\u0631\u06cc\u062a \u0627\u062f\u0645\u06cc\u0646", None))
        self.Admi_Name.setText(QCoreApplication.translate("Form", u"\u0627\u0633\u0645", None))
    # retranslateUi

