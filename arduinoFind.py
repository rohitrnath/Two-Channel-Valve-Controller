import serial.tools.list_ports
import threading
ports = list(serial.tools.list_ports.comports())
for p in ports:
    if 'USB' in p[2]:
        print (p)