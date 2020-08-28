
import xml.etree.ElementTree as ElementTree

class XmlHander:

    def __init__(self):
        self.devices = ElementTree.Element("devices")

    def write(self, device):
        device_sub = ElementTree.SubElement(self.devices, "device")
        device_address = ElementTree.SubElement(device_sub, "address", {"typ": "str"})
        device_name = ElementTree.SubElement(device_sub, "name", {"typ": "str"})

        for service in device.services:
            service_sub = ElementTree.SubElement(device_sub, "service")
            service_name = ElementTree.SubElement(service_sub, "name", {"typ": "str"})
            service_host = ElementTree.SubElement(service_sub, "host", {"typ": "str"})
            service_port = ElementTree.SubElement(service_sub, "port", {"typ": "str"})
            service_provider = ElementTree.SubElement(service_sub, "provider", {"typ": "str"})
            service_description = ElementTree.SubElement(service_sub, "description", {"typ": "str"})
            service_protocol = ElementTree.SubElement(service_sub, "protocol", {"typ": "str"})

            service_name.text = str(service.name)
            service_host.text = str(service.host)
            service_port.text = str(service.port)
            service_provider.text = str(service.provider)
            service_description.text = str(service.description)
            service_protocol.text = str(service.protocol)

        device_address.text = device.addr
        device_name.text = device.name

        et = ElementTree.ElementTree(self.devices)
        et.write("devices.xml")
