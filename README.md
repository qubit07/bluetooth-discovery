# Bluetooth Discovery

Build on Python 3.8.5 with PyBluez.

# XML Devices Output
<b>devices.xml</b>
```
<devices>
	<device>
		<address typ="str">A8:B9:6E:E7:D6:1E</address>
		<name typ="str">Nexus 5X</name>
	</device>
	<device>
		<address typ="str">B0:65:C1:FE:1C:B2</address>
		<name typ="str">PhilipsBT</name>
	</device>
	<device>
		<address typ="str">1C:00:2B:2C:48:EA</address>
		<name typ="str">Galaxy A40</name>
		<service>
			<name typ="str">b'Android Network Access Point\x00'</name>
			<host typ="str">1C:00:2B:2C:48:EA</host>
			<port typ="str">15</port>
			<provider typ="str">None</provider>
			<description typ="str">NAP</description>
			<protocol typ="str">L2CAP</protocol>
		</service>
		<service>
			<name typ="str">b'OBEX Phonebook Access Server\x00'</name>
			<host typ="str">1C:00:2B:2C:48:EA</host>
			<port typ="str">19</port>
			<provider typ="str">None</provider>
			<description typ="str"/>
			<protocol typ="str">RFCOMM</protocol>
		</service>
	</device>
</devices>
```
