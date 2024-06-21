import time
from db_utils import load_env_variables, get_connection_string, connect_to_database, insert_devices, insert_services
from bluetooth_utils import find_devs, find_services

load_env_variables()
conn_str = get_connection_string()
db = connect_to_database(conn_str)
print("connect to database: %s" % conn_str)

print("starting discover devices!")
while True:
    devices = find_devs()
    print("found number of devices: %s" % (len(devices.length)))
    insert_devices(devices)
    
    for (addr,name) in devices:
        services = find_services(addr)
        insert_services(services)
        time.sleep(1)

    time.sleep(5)


