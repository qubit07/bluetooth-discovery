import bluetooth
import time
import sqlite3
import threading
import logging
from xml_handler import XmlHander
from device import Device
from service import Service

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
                device = Device(addr, name)
                self.find_services(device)
                self.xmlHandler.write(device)

    def find_services(self, device):
        logging.log(logging.INFO,"start service discovery for addr: %s" % (device.addr))
        services = bluetooth.find_service(address=device.addr)

        for service in services:
            host = service['host']
            name = service['name']
            protocol = service['protocol']
            port = service['port']
            provider = service['provider']
            description = service['description']

            if name is not None:
                logging.log(logging.INFO,"found service: %s" % (name))
                s = Service(host, protocol, name, provider, port, description)
                device.add_service(s)
