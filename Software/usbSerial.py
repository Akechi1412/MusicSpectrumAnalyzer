from PySide6.QtSerialPort import QSerialPort
from PySide6.QtCore import QIODevice

class UsbSerial(QSerialPort):
    def __init__(self):
        super().__init__()

    def configure(self, baudrate, dataBits, parity, stopBits, flowControl):
        self.setBaudRate(baudrate)
        self.setDataBits(dataBits)
        self.setParity(parity)
        self.setStopBits(stopBits)
        self.setFlowControl(flowControl)

    def open_port(self):
        return self.open(QIODevice.ReadWrite)

    def close_port(self):
        self.close()
    