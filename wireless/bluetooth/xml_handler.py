
import xml.etree.ElementTree as ElementTree

class XmlHander:

    def __init__(self):
        self.devices = ElementTree.Element("devices")

    def write(self, addr, name):
        device = ElementTree.SubElement(self.devices, "device")
        addressSub = ElementTree.SubElement(device, "address", {"typ": "str"})
        nameSub = ElementTree.SubElement(device, "name", {"typ": "str"})

        addressSub.text = addr
        nameSub.text = name

        et = ElementTree.ElementTree(self.devices)
        et.write("devices.xml")
