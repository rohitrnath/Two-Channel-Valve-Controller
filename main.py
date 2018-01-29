# compliments of:    https://www.baldengineer.com/raspberry-pi-gui-tutorial.html
import sys
import threading
#Library for reading COM port details
import serial.tools.list_ports

# This gets the Qt stuff
import PyQt5
from PyQt5.QtWidgets import *
from serial_stuff import SerialCom

# This is our window from QtCreator
import mainwindow_auto

from serialThread import serialThreadClass

# create class for our Raspberry Pi GUI
class MainWindow(QMainWindow, mainwindow_auto.Ui_MainWindow):
    # access variables inside of the UI's file

    ### functions for the buttons to call
    def pressedInfuseCloseButton(self):
        print ("Pressed Infuse Close")
        #INSERT CODE
        #function should send a 'C' to the Arduino identified as 'I'
        self.mySerial1.sendSerial('C')

    def pressedInfuseOpenButton(self):
        print ("Pressed Infuse Open")
        #INSERT CODE
        #function should send a 'O' to the Arduino identified as 'I'
        self.mySerial1.sendSerial('O')


    def pressedDrainOpenButton(self):
        print ("Pressed Drain Open")
        #INSERT CODE
        #function should send a 'O' to the Arduino identified as 'D'
        self.mySerial2.sendSerial('O')


    def pressedDrainCloseButton(self):
        print ("Pressed Drain Close")
        #INSERT CODE
        #function should send a 'C' to the Arduino identified as 'D'
        self.mySerial2.sendSerial('C')

    def infuseData(self,data):
        print(data[2:9])
        if data[4] == 'C':
            self.updateInfuseValveState('Closed')
        elif data[4] == 'O':
            self.updateInfuseValveState('Open')

        self.updateInfuseWeight(str(int(data[5:9])))


    def drainData(self,data):
        print(data[2:9])
        if data[4] == 'C':
            self.updateDrainValveState('Closed')
        elif data[4] == 'O':
            self.updateDrainValveState('Open')

        self.updateDrainWeight(str(int(data[5:9])))



    def updateDrainValveState(self, state):
        #after receiving string from Drain-Arduino this should be called
        #to update the drain valve state
        self.lblDrainValveState.setText(state)

    def updateInfuseValveState(self, state):
        #after receiving string from Infuse-Arduino this should be called
        #to update the infuse valve state
        self.lblInfuseValveState.setText(state)

    def updateDrainWeight(self, weight):
        #after receiving string from Drain-Arduino this should be called
        #to update the drain weight
        self.lblDrainWeight.setText(weight)

    def updateInfuseWeight(self, weight):
        #after receiving string from Infuse-Arduino this should be called
        #to update the infuse weight
        self.lblInfuseWeight.setText(weight)


    def __init__(self,IF,DR):
        super(self.__class__, self).__init__()
        self.setupUi(self)  # gets defined in the UI file

        self.infuse = IF
        self.drain = DR

        ### Hooks for buttons

        self.btnInfuseClose.clicked.connect(lambda: self.pressedInfuseCloseButton())
        self.btnInfuseOpen.clicked.connect(lambda: self.pressedInfuseOpenButton())
        self.btnDrainOpen.clicked.connect(lambda: self.pressedDrainOpenButton())
        self.btnDrainClose.clicked.connect(lambda: self.pressedDrainCloseButton())  # I feel better having one of these

        self.mySerial1 = serialThreadClass(IF)
        self.mySerial2 = serialThreadClass(DR)

        # INSERT CODE
        # upon receipt of string from an Arduino, the string needs to be
        # parsed and the relevant data needs to be displayed to the GUI
        self.mySerial1.msg.connect(self.infuseData)
        self.mySerial2.msg.connect(self.drainData)


        self.mySerial1.start()  #startingInfuseSerialThread
        self.mySerial2.start()  #startingDrainSerialThread



def main():


    #INSERT CODE
    #need to search available COM ports and automatically connect
    #will be able to identify the Infuse-Arduino and Drain-Arduion
    #by sending an 'X' and expecting a reply of either 'I' or 'D'
    ports = list(serial.tools.list_ports.comports())
    COM = []
    for p in ports:
        if 'USB' in p[2]:
            print('Arduino may connected to : ' + p[0])
            COM.append(p[0])

    if len(COM) < 2 :
        print('Two arduinos are not connected properly')
        return

    for u in COM:
        SER = SerialCom(u)

        SER.writeData('X')
        kind = SER.readLine()

        if 'I' in kind :
            infuse = u
            print(u + ' is Infuse Arduino')

        elif 'D' in kind :
            drain = u
            print(u + ' is Drain Arduino')

    #INSERT CODE
    #once arduino connections are identified and made, need to set
    #monitoring for incoming strings of data from each Arduino.





    # a new app instance
    app = QApplication(sys.argv)
    form = MainWindow(infuse,drain)
    form.show()
    # without this, the script exits immediately.
    sys.exit(app.exec_())


# python bit to figure how who started This
if __name__ == "__main__":
    main()

