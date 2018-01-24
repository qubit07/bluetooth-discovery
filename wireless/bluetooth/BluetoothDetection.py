'''
Created on Nov 19, 2017

@author: qubit
'''

import bluetooth
import time
import sqlite3
import threading


def find_devs():
    print "discover devices..."
    devices = bluetooth.discover_devices(lookup_names=True)
    connection = connect_to_database();
    found_dev_list = get_dev_list(connection)

    for (addr ,name) in devices:
        if (addr,) not in found_dev_list:
	    print "found new device"
            insert_device(addr=addr, name=name, connection=connection)
            #t = threading.Thread(target=sdp_browse, args=(addr,))
            #t.start()
	    sdp_browse(addr)
           
def sdp_browse(addr):
    print "start sdp browsing..."
    services = bluetooth.find_service(address=addr)
    for service in services:
        host = service['host']
        name = service['name']
        protocol = service['protocol']
        port = service['port']
        provider = service['provider']
        description = service['description']
        insert_service(host,protocol, name, provider, port, description)
     
def create_database():
    print "create database"
    connection = connect_to_database()
    cursor = connection.cursor()
    try:
        cursor.execute("CREATE TABLE devices(host TEXT, name TEXT)")
    except:
        pass
    try:
        cursor.execute("CREATE TABLE services(host TEXT, protocol TEXT, name TEXT, provider TEXT, port INTEGER, description TEXT)")     
    except:
        pass
    connection.commit()

def connect_to_database(db_name='db/bluetooth.db'):
    connection = sqlite3.connect(db_name)
    return connection
 
def get_dev_list(connection):
    cursor = connection.cursor()
    cursor.execute("SELECT devices.host FROM devices")
    dev_list = cursor.fetchall()
    return dev_list

    
def insert_device(addr, name, connection):
    cursor = connection.cursor()
    connection.text_factory = str
    print "insert device mac: %s ,name: %s" %(addr,name)
    cursor.execute("INSERT INTO devices VALUES(?,?)",(addr, name))
    connection.commit()
    
    
def insert_service(host,protocol, name, provider, port, description):
    connection = connect_to_database()
    cursor = connection.cursor()
    connection.text_factory = str
    print "insert service host: %s - %s" %(host,name)
    cursor.execute("INSERT INTO services VALUES(?,?,?,?,?,?)",(host, protocol, name, provider, port, description))
    connection.commit()
    
     
if __name__ == '__main__':
    create_database()
    
    while True:
        find_devs()
        time.sleep(2)
   
