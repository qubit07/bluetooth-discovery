import os
from dotenv import load_dotenv
import sqlite3

def load_env_variables():
    dotenv_path = "../environment.env"
    load_dotenv(dotenv_path)

def get_connection_string():
    return os.getenv('DB_CONNECTION_STRING')

def connect_to_database(conn_str):
    if conn_str is None:
        raise ValueError("connection string not found in environment variables.")
    conn = sqlite3.connect(conn_str)
    return conn

def create_devices_table(conn):
    # Tabelle 'devices' erstellen, falls sie nicht existiert
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS devices (
            address TEXT PRIMARY KEY,
            name TEXT  
        )
    ''')
    conn.commit()

def create_services_table(conn):
    # Tabelle 'services' erstellen, falls sie nicht existiert
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS services (
            name TEXT,
            protocol TEXT,
            port INTEGER,
            PRIMARY KEY (name, protocol, port)
        )
    ''')
    conn.commit()

def insert_devices(conn, devices):
    cursor = conn.cursor()
    for (addr, name) in devices:
        cursor.execute('SELECT * FROM devices WHERE address=?', (addr,))
        existing_device = cursor.fetchone()

        if existing_device == None:
            cursor.execute('INSERT INTO devices (address, name) VALUES (?, ?)', (addr, name))
            conn.commit()
            print(f"add new device: address = {addr}, name = {name}")


def insert_services(conn, services):
    cursor = conn.cursor()
    for service in services:
        print(f"add new service:  name = {service['name']}, protocol = {service['protocol']}, port = {service['port']}")
        cursor.execute('SELECT * FROM services WHERE name=? AND protocol=? AND port=?', [service['name'], service['protocol'], service['port']])
        existing_device = cursor.fetchone()

        if existing_device == None and service['name'] != None:
            cursor.execute('INSERT INTO services (address, name) VALUES (?, ?, ?)', (service['name'], service['protocol'], service['port']))
            conn.commit()
            print(f"add new service:  name = {service['name']}, protocol = {service['protocol']}, port = {service['port']}")




