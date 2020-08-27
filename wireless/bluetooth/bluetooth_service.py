import bluetooth
import time
import sqlite3
import threading
import logging
from xml_handler import XmlHander

class BluetoothService:

    logging.basicConfig(filename = 'programm.log',
                        level = logging.DEBUG,
                        style = "{",
                        format = "{asctime} [{levelname:8}] {message}",
                        datefmt = "%d.%m.%Y %H:%M:%S")

    def __init__(self):
        self.found_devs = {'addr':'name'}
        self.xmlHandler = XmlHander()

    def connect(self):
        port = 1
        sock=bluetooth.BluetoothSocket( bluetooth.RFCOMM )
        sock.connect((addr, port))
        sock.send("#")
        sock.close()

    def find_devs(self):
        logging.log(logging.INFO,"starting discover devices")
        devices = bluetooth.discover_devices(lookup_names=True)
        for (addr,name) in devices:
            if (addr,) not in self.found_devs:
                logging.log(logging.INFO,"found new device: %s - %s" % (addr, name))
                self.found_devs.update({addr:name})
                self.xmlHandler.write(addr, name)
