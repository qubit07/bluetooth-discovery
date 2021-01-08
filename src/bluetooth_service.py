import bluetooth
from bluetooth_repository import BluetoothRepository

class BluetoothService:

    def __init__(self):
        self.found_devs = {'addr':'name'}
        BluetoothRepository.initialize()

    def find_devs(self):
        print("starting discover devices")
        devices = bluetooth.discover_devices(lookup_names=True)
        for (addr,name) in devices:
            if (addr,) not in self.found_devs:
                print("found device: %s - %s" % (addr, name))
                self.found_devs.update({addr:name})
                BluetoothRepository.insert('devices', {addr:name})     
                #self.find_services(addr)

    def find_services(self, addr):
        print("start service discovery for addr: %s" % (addr))
        services = bluetooth.find_service(address=addr)
        print(services)
        BluetoothRepository.insert('services', services)
     