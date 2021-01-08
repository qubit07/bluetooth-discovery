import bluetooth
from bluetooth_repository import BluetoothRepository

class BluetoothService:

    def __init__(self):
        BluetoothRepository.initialize()

    def find_devs(self):
        print("looking for devices...")
        devices = bluetooth.discover_devices(lookup_names=True)
        for (addr,name) in devices:
            device = BluetoothRepository.find_one('devices', {addr:name})

            if (device is None):
                print("found new device: %s - %s" % (addr, name))
                BluetoothRepository.insert('devices', {addr:name})
            else:
                print("skipping already discoverd device: %s - %s" % (addr, name))

    def find_services(self, addr):
        print("start service discovery for addr: %s" % (addr))
        services = bluetooth.find_service(address=addr)
        BluetoothRepository.insert('services', services)
     