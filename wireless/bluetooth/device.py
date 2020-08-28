class Device:
    def __init__(self, addr, name):
        self.addr = addr
        self.name = name
        self.services = []

    def add_service(self, service):
        self.services.append(service)
