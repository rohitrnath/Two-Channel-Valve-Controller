import serial
from PyQt5.QtCore import pyqtSignal,QThread

class serialThreadClass(QThread):
    msg = pyqtSignal(str)

    def __init__(self,port,parent=None):
        super(serialThreadClass,self).__init__(parent)
        self.seriport = serial.Serial()
        self.seriport.baudrate=9600
        self.seriport.port = port
        self.seriport.open()

    def run(self):
        while True:
            veri=self.seriport.readline()
            self.msg.emit(str(veri))
            #print(veri)

    def sendSerial(self,char):
        self.seriport.write(char.encode('ascii'))