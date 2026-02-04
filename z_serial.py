# -*- coding: utf-8 -*-
# requirements:
# pip install pyside6 pyserial

import sys
from datetime import datetime
import serial
import serial.tools.list_ports
from PySide6.QtCore import QThread, Signal, QTimer
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

    def open(self, port, baud, data_bits, parity, stop_bits):
        try:
            self.ser = serial.Serial(
                port,
                baud,
                bytesize=data_bits,
                parity=parity,
                stopbits=stop_bits,
                timeout=0.1,
            )
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

    def stop(self):
        self.running = False
        self.requestInterruption()


class SerialPortManager:
    def __init__(self):
        self.worker = SerialWorker()

    @property
    def data_received(self):
        return self.worker.data_received

    @property
    def status(self):
        return self.worker.status

    def open(self, port, baud, data_bits, parity, stop_bits):
        self.worker.open(port, baud, data_bits, parity, stop_bits)

    def close(self):
        self.worker.close()

    def send(self, data: bytes):
        self.worker.send(data)

    def stop(self):
        self.worker.stop()
        if self.worker.isRunning():
            self.worker.terminate()
            self.worker.wait(500)


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
        self.send_timer = QTimer(self)
        self.send_timer.setSingleShot(False)
        self.port_scan_timer = QTimer(self)
        self.port_scan_timer.setSingleShot(False)
        self._last_ports = []

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
        self.ui.clearRecvButton.clicked.connect(self.clear_recv)
        self.ui.clearSendButton.clicked.connect(self.ui.sendTextEdit.clear)
        self.ui.timedSendCheck.toggled.connect(self.toggle_timed_send)
        self.ui.intervalSpin.valueChanged.connect(self.update_timer_interval)
        self.send_timer.timeout.connect(self.send_data)
        self.ui.sendButton.setEnabled(False)
        self.ui.timedSendCheck.setEnabled(False)
        self._set_serial_config_enabled(True)
        self.port_scan_timer.timeout.connect(self._scan_ports)
        self.port_scan_timer.start(500)

    def _set_serial_config_enabled(self, enabled: bool):
        self.ui.portCombo.setEnabled(enabled)
        self.ui.baudCombo.setEnabled(enabled)
        self.ui.dataBitsCombo.setEnabled(enabled)
        self.ui.parityCombo.setEnabled(enabled)
        self.ui.stopBitsCombo.setEnabled(enabled)
        self.ui.refreshButton.setEnabled(enabled)

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
        self._last_ports = [p.device for p in ports]
        for p in ports:
            maker = p.manufacturer or ""
            extra = maker.strip()
            label = f"{p.device} {extra}".strip()
            self.ui.portCombo.addItem(label, p.device)

    def _scan_ports(self):
        ports = serial.tools.list_ports.comports()
        devices = [p.device for p in ports]
        if devices != self._last_ports:
            self.refresh_ports()
    
    def clear_recv(self):
        self.ui.recvTextEdit.clear()
        self.tx_count = 0
        self.rx_count = 0
        self.status_tx.setText(f"S:{str(self.tx_count)}")
        self.status_rx.setText(f"R:{str(self.rx_count)}")

    def toggle_serial(self):
        if self.ui.openButton.text() == "打开串口":
            port = self.ui.portCombo.currentData() or self.ui.portCombo.currentText().split()[0]
            baud = int(self.ui.baudCombo.currentText())
            data_bits = int(self.ui.dataBitsCombo.currentText())
            parity_text = self.ui.parityCombo.currentText()
            stop_bits_text = self.ui.stopBitsCombo.currentText()
            parity_map = {
                "None": serial.PARITY_NONE,
                "Even": serial.PARITY_EVEN,
                "Odd": serial.PARITY_ODD,
            }
            stop_bits_map = {
                "1": serial.STOPBITS_ONE,
                "1.5": serial.STOPBITS_ONE_POINT_FIVE,
                "2": serial.STOPBITS_TWO,
            }
            parity = parity_map.get(parity_text, serial.PARITY_NONE)
            stop_bits = stop_bits_map.get(stop_bits_text, serial.STOPBITS_ONE)
            self.serial.open(port, baud, data_bits, parity, stop_bits)
            self.ui.openButton.setText("关闭串口")
            self.status_port.setText(port or "未选择")
            self.status_line.setText(f"{port} 已打开 {baud}bps,{data_bits},{parity_text},{stop_bits_text}")
            self.ui.sendButton.setEnabled(True)
            self.ui.timedSendCheck.setEnabled(True)
            self._set_serial_config_enabled(False)
        else:
            if self.send_timer.isActive():
                self.send_timer.stop()
            if self.ui.timedSendCheck.isChecked():
                self.ui.timedSendCheck.setChecked(False)
            self.serial.close()
            self.ui.openButton.setText("打开串口")
            self.status_port.setText("未连接")
            self.status_line.setText("-")
            self.ui.sendButton.setEnabled(False)
            self.ui.timedSendCheck.setEnabled(False)
            self._set_serial_config_enabled(True)

    def send_data(self):
        if not self.serial.worker.ser or not self.serial.worker.ser.is_open:
            self.ui.recvTextEdit.append("[INFO] 串口未打开，无法发送")
            return
        text = self.ui.sendTextEdit.toPlainText()
        if not text:
            return
        if self.ui.hexSendCheck.isChecked():
            data = self._parse_hex_text(text)
            if data is None:
                self.ui.recvTextEdit.append("[INFO] HEX发送格式错误")
                return
        else:
            data = text.encode()
        if self.ui.splitDisplayCheck.isChecked():
            data += b"\n"
        self.serial.send(data)
        self.tx_count += len(data)
        self.status_tx.setText(f"S:{self.tx_count}")
        if self.ui.tsDisplayCheck.isChecked():
            timestamp = datetime.now().strftime("%H:%M:%S.%f")[:-3]
            send_text = self._format_bytes(
                data,
                self.ui.hexSendCheck.isChecked(),
                allow_split=False,
            )
            self.ui.recvTextEdit.append(f"[{timestamp}]发→◇{send_text}")

    def on_data(self, data: bytes):
        self.rx_count += len(data)
        self.status_rx.setText(f"R:{self.rx_count}")
        text = self._format_bytes(data, self.ui.hexDisplayCheck.isChecked())
        if self.ui.tsDisplayCheck.isChecked():
            timestamp = datetime.now().strftime("%H:%M:%S.%f")[:-3]
            self.ui.recvTextEdit.append(f"[{timestamp}]收←◆{text}")
        else:
            self.ui.recvTextEdit.moveCursor(QTextCursor.End)
            self.ui.recvTextEdit.insertPlainText(text)

    def on_status(self, msg):
        self.ui.recvTextEdit.append(f"[INFO] {msg}")
        if "ClearCommError failed" in msg:
            self._handle_serial_error_close()

    def _handle_serial_error_close(self):
        if self.send_timer.isActive():
            self.send_timer.stop()
        if self.ui.timedSendCheck.isChecked():
            self.ui.timedSendCheck.setChecked(False)
        self.serial.close()
        self.ui.openButton.setText("打开串口")
        self.status_port.setText("未连接")
        self.status_line.setText("-")
        self.ui.sendButton.setEnabled(False)
        self.ui.timedSendCheck.setEnabled(False)
        self._set_serial_config_enabled(True)
        self.refresh_ports()

    def toggle_timed_send(self, checked: bool):
        if checked and (not self.serial.worker.ser or not self.serial.worker.ser.is_open):
            self.ui.recvTextEdit.append("[INFO] 串口未打开，无法定时发送")
            self.ui.timedSendCheck.setChecked(False)
            return
        if checked:
            if not self.send_timer.isActive():
                self.send_timer.start(self.ui.intervalSpin.value())
        else:
            if self.send_timer.isActive():
                self.send_timer.stop()

    def update_timer_interval(self, value: int):
        if self.send_timer.isActive():
            self.send_timer.start(value)

    def _format_bytes(self, data: bytes, hex_mode: bool, allow_split: bool = True) -> str:
        add_newline = allow_split and self.ui.splitDisplayCheck.isChecked()
        if hex_mode:
            sep = "\n" if add_newline else " "
            return sep.join(f"{b:02X}" for b in data)
        text = data.decode(errors='ignore')
        return f"{text}\n" if add_newline else text

    def _parse_hex_text(self, text: str):
        cleaned = text.replace("0x", " ").replace(",", " ").replace("\n", " ").replace("\t", " ")
        parts = [p for p in cleaned.split(" ") if p]
        if not parts:
            return b""
        if len(parts) == 1:
            raw = parts[0]
            if len(raw) % 2 != 0:
                return None
            try:
                return bytes.fromhex(raw)
            except ValueError:
                return None
        try:
            return bytes(int(p, 16) for p in parts)
        except ValueError:
            return None

    def closeEvent(self, event):
        if self.send_timer.isActive():
            self.send_timer.stop()
        if self.port_scan_timer.isActive():
            self.port_scan_timer.stop()
        if self.ui.timedSendCheck.isChecked():
            self.ui.timedSendCheck.setChecked(False)
        self.serial.close()
        self.serial.stop()
        event.accept()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = SerialAssistant()
    w.show()
    sys.exit(app.exec())
