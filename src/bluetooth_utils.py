import bluetooth

def find_devs():
    print("looking for devices...")
    return bluetooth.discover_devices(lookup_names=True)

def find_services(addr):
    print("start service discovery for addr: %s" % (addr))
    return bluetooth.find_service(address=addr)