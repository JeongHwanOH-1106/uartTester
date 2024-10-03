# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'UartGCS.ui'
##
## Created by: Qt User Interface Compiler version 6.4.2
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
from PySide6.QtWidgets import (QApplication, QFormLayout, QLabel, QLineEdit,
    QMainWindow, QMenuBar, QPushButton, QSizePolicy,
    QStatusBar, QTextEdit, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(388, 454)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.formLayout = QFormLayout(self.centralwidget)
        self.formLayout.setObjectName(u"formLayout")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label)

        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label_2)

        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.pushButton)

        self.pushButton_2 = QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName(u"pushButton_2")

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.pushButton_2)

        self.lineEdit = QLineEdit(self.centralwidget)
        self.lineEdit.setObjectName(u"lineEdit")

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.lineEdit)

        self.pushButton_3 = QPushButton(self.centralwidget)
        self.pushButton_3.setObjectName(u"pushButton_3")

        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.pushButton_3)

        self.textEdit = QTextEdit(self.centralwidget)
        self.textEdit.setObjectName(u"textEdit")

        self.formLayout.setWidget(11, QFormLayout.SpanningRole, self.textEdit)

        self.lineEdit_2 = QLineEdit(self.centralwidget)
        self.lineEdit_2.setObjectName(u"lineEdit_2")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.lineEdit_2)

        self.lineEdit_3 = QLineEdit(self.centralwidget)
        self.lineEdit_3.setObjectName(u"lineEdit_3")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.lineEdit_3)

        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")

        self.formLayout.setWidget(9, QFormLayout.LabelRole, self.label_3)

        self.val_the = QLabel(self.centralwidget)
        self.val_the.setObjectName(u"val_the")

        self.formLayout.setWidget(9, QFormLayout.FieldRole, self.val_the)

        self.label_5 = QLabel(self.centralwidget)
        self.label_5.setObjectName(u"label_5")

        self.formLayout.setWidget(5, QFormLayout.LabelRole, self.label_5)

        self.label_6 = QLabel(self.centralwidget)
        self.label_6.setObjectName(u"label_6")

        self.formLayout.setWidget(4, QFormLayout.LabelRole, self.label_6)

        self.label_8 = QLabel(self.centralwidget)
        self.label_8.setObjectName(u"label_8")

        self.formLayout.setWidget(8, QFormLayout.LabelRole, self.label_8)

        self.label_9 = QLabel(self.centralwidget)
        self.label_9.setObjectName(u"label_9")

        self.formLayout.setWidget(7, QFormLayout.LabelRole, self.label_9)

        self.val_Psi_cmd = QLabel(self.centralwidget)
        self.val_Psi_cmd.setObjectName(u"val_Psi_cmd")

        self.formLayout.setWidget(8, QFormLayout.FieldRole, self.val_Psi_cmd)

        self.label_10 = QLabel(self.centralwidget)
        self.label_10.setObjectName(u"label_10")

        self.formLayout.setWidget(10, QFormLayout.LabelRole, self.label_10)

        self.val_psi = QLabel(self.centralwidget)
        self.val_psi.setObjectName(u"val_psi")

        self.formLayout.setWidget(10, QFormLayout.FieldRole, self.val_psi)

        self.val_The_cmd = QLabel(self.centralwidget)
        self.val_The_cmd.setObjectName(u"val_The_cmd")

        self.formLayout.setWidget(7, QFormLayout.FieldRole, self.val_The_cmd)

        self.val_Phi_cmd = QLabel(self.centralwidget)
        self.val_Phi_cmd.setObjectName(u"val_Phi_cmd")

        self.formLayout.setWidget(5, QFormLayout.FieldRole, self.val_Phi_cmd)

        self.val_cnt = QLabel(self.centralwidget)
        self.val_cnt.setObjectName(u"val_cnt")

        self.formLayout.setWidget(4, QFormLayout.FieldRole, self.val_cnt)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 388, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.pushButton.clicked.connect(MainWindow.port_open)
        self.pushButton_2.clicked.connect(MainWindow.port_close)
        self.pushButton_3.clicked.connect(MainWindow.serial_send)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"IP :", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Port :", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Open", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"Close", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"Send", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"pitch", None))
        self.val_the.setText(QCoreApplication.translate("MainWindow", u"val_the", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Phi_cmd", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Count", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Psi_cmd", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"The_cmd", None))
        self.val_Psi_cmd.setText(QCoreApplication.translate("MainWindow", u"val_Psi_cmd", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"yaw", None))
        self.val_psi.setText(QCoreApplication.translate("MainWindow", u"val_psi", None))
        self.val_The_cmd.setText(QCoreApplication.translate("MainWindow", u"val_The_cmd", None))
        self.val_Phi_cmd.setText(QCoreApplication.translate("MainWindow", u"val_Phi_cmd", None))
        self.val_cnt.setText(QCoreApplication.translate("MainWindow", u"Count", None))
    # retranslateUi

