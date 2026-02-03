# -*- coding: utf-8 -*-

from PySide6 import QtCore, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(820, 620)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.mainLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.mainLayout.setContentsMargins(6, 6, 6, 4)
        self.mainLayout.setSpacing(6)
        self.recvTextEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.recvTextEdit.setReadOnly(True)
        self.recvTextEdit.setPlaceholderText("接收区")
        self.mainLayout.addWidget(self.recvTextEdit)

        self.midPanel = QtWidgets.QFrame(self.centralwidget)
        self.midPanel.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.midLayout = QtWidgets.QGridLayout(self.midPanel)
        self.midLayout.setContentsMargins(6, 6, 6, 6)
        self.midLayout.setHorizontalSpacing(8)
        self.midLayout.setVerticalSpacing(4)

        self.portLabel = QtWidgets.QLabel("端口号", self.midPanel)
        self.midLayout.addWidget(self.portLabel, 0, 0)

        self.portCombo = QtWidgets.QComboBox(self.midPanel)
        self.midLayout.addWidget(self.portCombo, 0, 1, 1, 2)

        self.refreshButton = QtWidgets.QPushButton("刷新", self.midPanel)
        self.midLayout.addWidget(self.refreshButton, 0, 3)

        self.openButton = QtWidgets.QPushButton("打开串口", self.midPanel)
        self.midLayout.addWidget(self.openButton, 0, 5, 1, 3)

        self.baudLabel = QtWidgets.QLabel("波特率", self.midPanel)
        self.midLayout.addWidget(self.baudLabel, 1, 0)

        self.baudCombo = QtWidgets.QComboBox(self.midPanel)
        self.midLayout.addWidget(self.baudCombo, 1, 1)

        self.dataBitsLabel = QtWidgets.QLabel("数据位", self.midPanel)
        self.midLayout.addWidget(self.dataBitsLabel, 1, 2)

        self.dataBitsCombo = QtWidgets.QComboBox(self.midPanel)
        self.midLayout.addWidget(self.dataBitsCombo, 1, 3)

        self.parityLabel = QtWidgets.QLabel("校验", self.midPanel)
        self.midLayout.addWidget(self.parityLabel, 1, 4)

        self.parityCombo = QtWidgets.QComboBox(self.midPanel)
        self.midLayout.addWidget(self.parityCombo, 1, 5)

        self.stopBitsLabel = QtWidgets.QLabel("停止位", self.midPanel)
        self.midLayout.addWidget(self.stopBitsLabel, 1, 6)

        self.stopBitsCombo = QtWidgets.QComboBox(self.midPanel)
        self.midLayout.addWidget(self.stopBitsCombo, 1, 7)

        self.hexDisplayCheck = QtWidgets.QCheckBox("HEX显示", self.midPanel)
        self.midLayout.addWidget(self.hexDisplayCheck, 2, 0, 1, 2)

        self.tsDisplayCheck = QtWidgets.QCheckBox("加时间戳", self.midPanel)
        self.midLayout.addWidget(self.tsDisplayCheck, 2, 2, 1, 2)

        self.splitDisplayCheck = QtWidgets.QCheckBox("加间隔符", self.midPanel)
        self.midLayout.addWidget(self.splitDisplayCheck, 2, 4, 1, 2)

        self.mainLayout.addWidget(self.midPanel)

        self.sendPanel = QtWidgets.QFrame(self.centralwidget)
        self.sendPanel.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.sendLayout = QtWidgets.QGridLayout(self.sendPanel)
        self.sendLayout.setContentsMargins(6, 6, 6, 6)
        self.sendLayout.setHorizontalSpacing(8)
        self.sendLayout.setVerticalSpacing(4)

        self.sendTextEdit = QtWidgets.QTextEdit(self.sendPanel)
        self.sendTextEdit.setPlaceholderText("发送区")
        self.sendTextEdit.setMinimumHeight(90)
        self.sendTextEdit.setMaximumHeight(90)
        self.sendLayout.addWidget(self.sendTextEdit, 0, 0, 2, 6)

        self.sendButton = QtWidgets.QPushButton("发送", self.sendPanel)
        self.sendLayout.addWidget(self.sendButton, 0, 6)

        self.clearRecvButton = QtWidgets.QPushButton("清除接收", self.sendPanel)
        self.sendLayout.addWidget(self.clearRecvButton, 1, 6)

        self.clearSendButton = QtWidgets.QPushButton("清除发送", self.sendPanel)
        self.sendLayout.addWidget(self.clearSendButton, 0, 7)

        self.hexSendCheck = QtWidgets.QCheckBox("HEX发送", self.sendPanel)
        self.sendLayout.addWidget(self.hexSendCheck, 2, 0)

        self.timedSendCheck = QtWidgets.QCheckBox("定时发送", self.sendPanel)
        self.sendLayout.addWidget(self.timedSendCheck, 2, 1)

        self.intervalSpin = QtWidgets.QSpinBox(self.sendPanel)
        self.intervalSpin.setMinimum(10)
        self.intervalSpin.setMaximum(10000)
        self.intervalSpin.setValue(100)
        self.sendLayout.addWidget(self.intervalSpin, 2, 2)

        self.intervalLabel = QtWidgets.QLabel("ms/次", self.sendPanel)
        self.sendLayout.addWidget(self.intervalLabel, 2, 3)

        self.mainLayout.addWidget(self.sendPanel)

        MainWindow.setCentralWidget(self.centralwidget)

        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 820, 22))
        MainWindow.setMenuBar(self.menubar)
        self.menuComm = QtWidgets.QMenu("通讯端口", self.menubar)
        self.menuSerial = QtWidgets.QMenu("串口设置", self.menubar)
        self.menuDisplay = QtWidgets.QMenu("显示", self.menubar)
        self.menuSend = QtWidgets.QMenu("发送", self.menubar)
        self.menuMulti = QtWidgets.QMenu("多字符串", self.menubar)
        self.menuTools = QtWidgets.QMenu("小工具", self.menubar)
        self.menuHelp = QtWidgets.QMenu("帮助", self.menubar)
        self.menuContact = QtWidgets.QMenu("联系作者", self.menubar)
        self.menuSite = QtWidgets.QMenu("大白电子", self.menubar)
        self.menubar.addAction(self.menuComm.menuAction())
        self.menubar.addAction(self.menuSerial.menuAction())
        self.menubar.addAction(self.menuDisplay.menuAction())
        self.menubar.addAction(self.menuSend.menuAction())
        self.menubar.addAction(self.menuMulti.menuAction())
        self.menubar.addAction(self.menuTools.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())
        self.menubar.addAction(self.menuContact.menuAction())
        self.menubar.addAction(self.menuSite.menuAction())

        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle("串口/网络数据调试助手")


