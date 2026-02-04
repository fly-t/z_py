# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'serial.ui'
##
## Created by: Qt User Interface Compiler version 6.9.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QFrame,
    QGridLayout, QLabel, QMainWindow, QMenu,
    QMenuBar, QPushButton, QSizePolicy, QSpinBox,
    QStatusBar, QTextEdit, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(820, 620)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.mainLayout = QVBoxLayout(self.centralwidget)
        self.mainLayout.setSpacing(6)
        self.mainLayout.setObjectName(u"mainLayout")
        self.mainLayout.setContentsMargins(6, 6, 6, 4)
        self.recvTextEdit = QTextEdit(self.centralwidget)
        self.recvTextEdit.setObjectName(u"recvTextEdit")
        self.recvTextEdit.setReadOnly(True)

        self.mainLayout.addWidget(self.recvTextEdit)

        self.midPanel = QFrame(self.centralwidget)
        self.midPanel.setObjectName(u"midPanel")
        self.midPanel.setFrameShape(QFrame.StyledPanel)
        self.midLayout = QGridLayout(self.midPanel)
        self.midLayout.setObjectName(u"midLayout")
        self.midLayout.setHorizontalSpacing(8)
        self.midLayout.setVerticalSpacing(4)
        self.midLayout.setContentsMargins(6, 6, 6, 6)
        self.portLabel = QLabel(self.midPanel)
        self.portLabel.setObjectName(u"portLabel")

        self.midLayout.addWidget(self.portLabel, 0, 0, 1, 1)

        self.portCombo = QComboBox(self.midPanel)
        self.portCombo.setObjectName(u"portCombo")

        self.midLayout.addWidget(self.portCombo, 0, 1, 1, 2)

        self.refreshButton = QPushButton(self.midPanel)
        self.refreshButton.setObjectName(u"refreshButton")

        self.midLayout.addWidget(self.refreshButton, 0, 3, 1, 1)

        self.openButton = QPushButton(self.midPanel)
        self.openButton.setObjectName(u"openButton")

        self.midLayout.addWidget(self.openButton, 0, 5, 1, 3)

        self.baudLabel = QLabel(self.midPanel)
        self.baudLabel.setObjectName(u"baudLabel")

        self.midLayout.addWidget(self.baudLabel, 1, 0, 1, 1)

        self.baudCombo = QComboBox(self.midPanel)
        self.baudCombo.setObjectName(u"baudCombo")

        self.midLayout.addWidget(self.baudCombo, 1, 1, 1, 1)

        self.dataBitsLabel = QLabel(self.midPanel)
        self.dataBitsLabel.setObjectName(u"dataBitsLabel")

        self.midLayout.addWidget(self.dataBitsLabel, 1, 2, 1, 1)

        self.dataBitsCombo = QComboBox(self.midPanel)
        self.dataBitsCombo.setObjectName(u"dataBitsCombo")

        self.midLayout.addWidget(self.dataBitsCombo, 1, 3, 1, 1)

        self.parityLabel = QLabel(self.midPanel)
        self.parityLabel.setObjectName(u"parityLabel")

        self.midLayout.addWidget(self.parityLabel, 1, 4, 1, 1)

        self.parityCombo = QComboBox(self.midPanel)
        self.parityCombo.setObjectName(u"parityCombo")

        self.midLayout.addWidget(self.parityCombo, 1, 5, 1, 1)

        self.stopBitsLabel = QLabel(self.midPanel)
        self.stopBitsLabel.setObjectName(u"stopBitsLabel")

        self.midLayout.addWidget(self.stopBitsLabel, 1, 6, 1, 1)

        self.stopBitsCombo = QComboBox(self.midPanel)
        self.stopBitsCombo.setObjectName(u"stopBitsCombo")

        self.midLayout.addWidget(self.stopBitsCombo, 1, 7, 1, 1)

        self.hexDisplayCheck = QCheckBox(self.midPanel)
        self.hexDisplayCheck.setObjectName(u"hexDisplayCheck")

        self.midLayout.addWidget(self.hexDisplayCheck, 2, 0, 1, 2)

        self.tsDisplayCheck = QCheckBox(self.midPanel)
        self.tsDisplayCheck.setObjectName(u"tsDisplayCheck")

        self.midLayout.addWidget(self.tsDisplayCheck, 2, 2, 1, 2)

        self.splitDisplayCheck = QCheckBox(self.midPanel)
        self.splitDisplayCheck.setObjectName(u"splitDisplayCheck")

        self.midLayout.addWidget(self.splitDisplayCheck, 2, 4, 1, 2)


        self.mainLayout.addWidget(self.midPanel)

        self.sendPanel = QFrame(self.centralwidget)
        self.sendPanel.setObjectName(u"sendPanel")
        self.sendPanel.setFrameShape(QFrame.StyledPanel)
        self.sendLayout = QGridLayout(self.sendPanel)
        self.sendLayout.setObjectName(u"sendLayout")
        self.sendLayout.setHorizontalSpacing(8)
        self.sendLayout.setVerticalSpacing(4)
        self.sendLayout.setContentsMargins(6, 6, 6, 6)
        self.sendTextEdit = QTextEdit(self.sendPanel)
        self.sendTextEdit.setObjectName(u"sendTextEdit")
        self.sendTextEdit.setMinimumHeight(90)
        self.sendTextEdit.setMaximumHeight(90)

        self.sendLayout.addWidget(self.sendTextEdit, 0, 0, 2, 6)

        self.sendButton = QPushButton(self.sendPanel)
        self.sendButton.setObjectName(u"sendButton")

        self.sendLayout.addWidget(self.sendButton, 0, 6, 1, 1)

        self.clearRecvButton = QPushButton(self.sendPanel)
        self.clearRecvButton.setObjectName(u"clearRecvButton")

        self.sendLayout.addWidget(self.clearRecvButton, 1, 6, 1, 1)

        self.clearSendButton = QPushButton(self.sendPanel)
        self.clearSendButton.setObjectName(u"clearSendButton")

        self.sendLayout.addWidget(self.clearSendButton, 0, 7, 1, 1)

        self.hexSendCheck = QCheckBox(self.sendPanel)
        self.hexSendCheck.setObjectName(u"hexSendCheck")

        self.sendLayout.addWidget(self.hexSendCheck, 2, 0, 1, 1)

        self.timedSendCheck = QCheckBox(self.sendPanel)
        self.timedSendCheck.setObjectName(u"timedSendCheck")

        self.sendLayout.addWidget(self.timedSendCheck, 2, 1, 1, 1)

        self.intervalSpin = QSpinBox(self.sendPanel)
        self.intervalSpin.setObjectName(u"intervalSpin")
        self.intervalSpin.setMinimum(10)
        self.intervalSpin.setMaximum(10000)
        self.intervalSpin.setValue(100)

        self.sendLayout.addWidget(self.intervalSpin, 2, 2, 1, 1)

        self.intervalLabel = QLabel(self.sendPanel)
        self.intervalLabel.setObjectName(u"intervalLabel")

        self.sendLayout.addWidget(self.intervalLabel, 2, 3, 1, 1)


        self.mainLayout.addWidget(self.sendPanel)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 820, 22))
        self.menuComm = QMenu(self.menubar)
        self.menuComm.setObjectName(u"menuComm")
        self.menuSerial = QMenu(self.menubar)
        self.menuSerial.setObjectName(u"menuSerial")
        self.menuDisplay = QMenu(self.menubar)
        self.menuDisplay.setObjectName(u"menuDisplay")
        self.menuSend = QMenu(self.menubar)
        self.menuSend.setObjectName(u"menuSend")
        self.menuMulti = QMenu(self.menubar)
        self.menuMulti.setObjectName(u"menuMulti")
        self.menuTools = QMenu(self.menubar)
        self.menuTools.setObjectName(u"menuTools")
        self.menuHelp = QMenu(self.menubar)
        self.menuHelp.setObjectName(u"menuHelp")
        self.menuContact = QMenu(self.menubar)
        self.menuContact.setObjectName(u"menuContact")
        self.menuSite = QMenu(self.menubar)
        self.menuSite.setObjectName(u"menuSite")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuComm.menuAction())
        self.menubar.addAction(self.menuSerial.menuAction())
        self.menubar.addAction(self.menuDisplay.menuAction())
        self.menubar.addAction(self.menuSend.menuAction())
        self.menubar.addAction(self.menuMulti.menuAction())
        self.menubar.addAction(self.menuTools.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())
        self.menubar.addAction(self.menuContact.menuAction())
        self.menubar.addAction(self.menuSite.menuAction())

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"\u4e32\u53e3/\u7f51\u7edc\u6570\u636e\u8c03\u8bd5\u52a9\u624b", None))
        self.recvTextEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u63a5\u6536\u533a", None))
        self.portLabel.setText(QCoreApplication.translate("MainWindow", u"\u7aef\u53e3\u53f7", None))
        self.refreshButton.setText(QCoreApplication.translate("MainWindow", u"\u5237\u65b0", None))
        self.openButton.setText(QCoreApplication.translate("MainWindow", u"\u6253\u5f00\u4e32\u53e3", None))
        self.baudLabel.setText(QCoreApplication.translate("MainWindow", u"\u6ce2\u7279\u7387", None))
        self.dataBitsLabel.setText(QCoreApplication.translate("MainWindow", u"\u6570\u636e\u4f4d", None))
        self.parityLabel.setText(QCoreApplication.translate("MainWindow", u"\u6821\u9a8c", None))
        self.stopBitsLabel.setText(QCoreApplication.translate("MainWindow", u"\u505c\u6b62\u4f4d", None))
        self.hexDisplayCheck.setText(QCoreApplication.translate("MainWindow", u"HEX\u663e\u793a", None))
        self.tsDisplayCheck.setText(QCoreApplication.translate("MainWindow", u"\u52a0\u65f6\u95f4\u6233", None))
        self.splitDisplayCheck.setText(QCoreApplication.translate("MainWindow", u"\u52a0\u95f4\u9694\u7b26", None))
        self.sendTextEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u53d1\u9001\u533a", None))
        self.sendButton.setText(QCoreApplication.translate("MainWindow", u"\u53d1\u9001", None))
        self.clearRecvButton.setText(QCoreApplication.translate("MainWindow", u"\u6e05\u9664\u63a5\u6536", None))
        self.clearSendButton.setText(QCoreApplication.translate("MainWindow", u"\u6e05\u9664\u53d1\u9001", None))
        self.hexSendCheck.setText(QCoreApplication.translate("MainWindow", u"HEX\u53d1\u9001", None))
        self.timedSendCheck.setText(QCoreApplication.translate("MainWindow", u"\u5b9a\u65f6\u53d1\u9001", None))
        self.intervalLabel.setText(QCoreApplication.translate("MainWindow", u"ms/\u6b21", None))
        self.menuComm.setTitle(QCoreApplication.translate("MainWindow", u"\u901a\u8baf\u7aef\u53e3", None))
        self.menuSerial.setTitle(QCoreApplication.translate("MainWindow", u"\u4e32\u53e3\u8bbe\u7f6e", None))
        self.menuDisplay.setTitle(QCoreApplication.translate("MainWindow", u"\u663e\u793a", None))
        self.menuSend.setTitle(QCoreApplication.translate("MainWindow", u"\u53d1\u9001", None))
        self.menuMulti.setTitle(QCoreApplication.translate("MainWindow", u"\u591a\u5b57\u7b26\u4e32", None))
        self.menuTools.setTitle(QCoreApplication.translate("MainWindow", u"\u5c0f\u5de5\u5177", None))
        self.menuHelp.setTitle(QCoreApplication.translate("MainWindow", u"\u5e2e\u52a9", None))
        self.menuContact.setTitle(QCoreApplication.translate("MainWindow", u"\u8054\u7cfb\u4f5c\u8005", None))
        self.menuSite.setTitle(QCoreApplication.translate("MainWindow", u"\u5927\u767d\u7535\u5b50", None))
    # retranslateUi

