import time
from db_utils import load_env_variables, get_mongo_connection_string, connect_to_mongo, insert_devices, insert_services
from bluetooth_utils import find_devs, find_services

load_env_variables()
mongo_conn_str = get_mongo_connection_string()
db = connect_to_mongo(mongo_conn_str)

print("starting discover devices!")
while True:
    devices = find_devs()
    print("found number of devices: %s" % (len(devices.length)))
    insert_devices(devices)
    
    for (addr,name) in devices:
        services = find_services(addr)
        print(f"found services for addr = {addr},  services = {len(services)}")
        insert_services(services)
        time.sleep(1)


    time.sleep(5)


