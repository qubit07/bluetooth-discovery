import time
from db_utils import load_env_variables, get_connection_string, connect_to_database, insert_devices, insert_services, create_devices_table, create_services_table
from bluetooth_utils import find_devs, find_services

load_env_variables()
conn_str = get_connection_string()
db = connect_to_database(conn_str)
create_devices_table(db)
create_services_table(db)
print("connect to database: %s" % conn_str)

print("starting discover devices!")
while True:
    devices = find_devs()
    print("found number of devices: %s" % (len(devices)))
    insert_devices(db, devices)
    
    for (addr,name) in devices:
        services = find_services(addr)
        insert_services(db, services)
        time.sleep(1)

    time.sleep(5)


