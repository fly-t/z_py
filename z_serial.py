# -*- coding: utf-8 -*-
# requirements:
# pip install pyside6 pyserial

import sys
from datetime import datetime
import serial
import serial.tools.list_ports
from PySide6.QtCore import QThread, Signal
from PySide6.QtGui import QTextCursor
from PySide6.QtWidgets import QApplication, QMainWindow, QLabel, QStatusBar

from ui_serial import Ui_MainWindow


class SerialWorker(QThread):
    data_received = Signal(bytes)
    status = Signal(str)

    def __init__(self):
        super().__init__()
        self.ser = None
        self.running = False

    def open(self, port, baud):
        try:
            self.ser = serial.Serial(port, baud, timeout=0.1)
            self.running = True
            if not self.isRunning():
                self.start()
            self.status.emit(f"打开串口 {port} @ {baud}")
        except Exception as e:
            self.status.emit(str(e))

    def close(self):
        self.running = False
        if self.ser:
            self.ser.close()
            self.ser = None
        self.status.emit("串口已关闭")

    def send(self, data: bytes):
        if self.ser and self.ser.is_open:
            self.ser.write(data)

    def run(self):
        while True:
            if self.running and self.ser:
                try:
                    data = self.ser.read(1024)
                    if data:
                        self.data_received.emit(data)
                except Exception as e:
                    self.status.emit(str(e))
            self.msleep(5)


class SerialPortManager:
    def __init__(self):
        self.worker = SerialWorker()

    @property
    def data_received(self):
        return self.worker.data_received

    @property
    def status(self):
        return self.worker.status

    def open(self, port, baud):
        self.worker.open(port, baud)

    def close(self):
        self.worker.close()

    def send(self, data: bytes):
        self.worker.send(data)


class SerialAssistant(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.serial = SerialPortManager()
        self.serial.data_received.connect(self.on_data)
        self.serial.status.connect(self.on_status)

        self.tx_count = 0
        self.rx_count = 0

        self._init_controls()
        self._build_status()

    def _init_controls(self):
        self.ui.baudCombo.addItems(["9600", "115200", "921600"])
        self.ui.dataBitsCombo.addItems(["8", "7", "6", "5"])
        self.ui.parityCombo.addItems(["None", "Even", "Odd"])
        self.ui.stopBitsCombo.addItems(["1", "1.5", "2"])

        self.refresh_ports()

        self.ui.openButton.clicked.connect(self.toggle_serial)
        self.ui.refreshButton.clicked.connect(self.refresh_ports)
        self.ui.sendButton.clicked.connect(self.send_data)
        self.ui.clearRecvButton.clicked.connect(self.ui.recvTextEdit.clear)
        self.ui.clearSendButton.clicked.connect(self.ui.sendTextEdit.clear)

    def _build_status(self):
        bar = QStatusBar()
        self.status_port = QLabel("未连接")
        self.status_tx = QLabel("S:0")
        self.status_rx = QLabel("R:0")
        self.status_line = QLabel("-")

        bar.addWidget(self.status_port)
        bar.addWidget(self.status_tx)
        bar.addWidget(self.status_rx)
        bar.addWidget(self.status_line, 1)
        self.setStatusBar(bar)

    def refresh_ports(self):
        self.ui.portCombo.clear()
        ports = serial.tools.list_ports.comports()
        for p in ports:
            maker = p.manufacturer or ""
            extra = maker.strip()
            label = f"{p.device} {extra}".strip()
            self.ui.portCombo.addItem(label, p.device)

    def toggle_serial(self):
        if self.ui.openButton.text() == "打开串口":
            port = self.ui.portCombo.currentData() or self.ui.portCombo.currentText().split()[0]
            baud = int(self.ui.baudCombo.currentText())
            self.serial.open(port, baud)
            self.ui.openButton.setText("关闭串口")
            self.status_port.setText(port or "未选择")
            self.status_line.setText(f"{port} 已打开 {baud}bps,8,N,1")
        else:
            self.serial.close()
            self.ui.openButton.setText("打开串口")
            self.status_port.setText("未连接")
            self.status_line.setText("-")

    def send_data(self):
        text = self.ui.sendTextEdit.toPlainText()
        if not text:
            return
        data = text.encode()
        self.serial.send(data)
        self.tx_count += len(data)
        self.status_tx.setText(f"S:{self.tx_count}")
        timestamp = datetime.now().strftime("%H:%M:%S.%f")[:-3]
        self.ui.recvTextEdit.append(f"[{timestamp}]发→◇{text}")

    def on_data(self, data: bytes):
        self.rx_count += len(data)
        self.status_rx.setText(f"R:{self.rx_count}")
        text = data.decode(errors='ignore')
        timestamp = datetime.now().strftime("%H:%M:%S.%f")[:-3]
        self.ui.recvTextEdit.append(f"[{timestamp}]收←◆{text}")

    def on_status(self, msg):
        self.ui.recvTextEdit.append(f"[INFO] {msg}")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = SerialAssistant()
    w.show()
    sys.exit(app.exec())
