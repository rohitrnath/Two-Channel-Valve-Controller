import serial
import time

#this entire class is just a crude start
#at some serial connection.  Sorta works

class SerialCom():
    def __init__(self, portName):
        super(self.__class__, self).__init__()
        self.portName = portName

    #def openPort(self):
        self.ser = serial.Serial(
            port = self.portName,
            baudrate=9600,
            parity=serial.PARITY_NONE,
            stopbits=serial.STOPBITS_ONE,
            bytesize=serial.EIGHTBITS,
            timeout=1
        )
        time.sleep(2)

       # return ser

    def readLine(self):

        while 1:
            #
            try:
                if (self.ser.inWaiting() > 0):
                    ack = self.ser.readline().decode('ascii')
                    if ack:
                        ack = ack.rstrip()
                        return ack
                #time.sleep(1)
            except self.ser.SerialTimeoutException:
                print("Data could not be read")


    def writeData(self,char):
        self.ser.write(char.encode('ascii'))
        #self.ser.flush()


