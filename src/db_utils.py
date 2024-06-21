import os
from dotenv import load_dotenv
from pymongo import MongoClient

def load_env_variables():
    dotenv_path = "../environment.env"
    load_dotenv(dotenv_path)

def get_mongo_connection_string():
    return os.getenv('MONGO_CONNECTION_STRING')

def connect_to_mongo(mongo_conn_str):
    if mongo_conn_str is None:
        raise ValueError("mongoDB connection string not found in environment variables.")
    client = MongoClient(mongo_conn_str)
    db = client.get_database()
    return db

def insert_devices(db, devices):
    collection = db['devices']
    for device in devices:
          if not collection.find_one({"addr": device["addr"]}):
            collection.insert_one(device)
            print(f"add new device: Addr = {device['addr']}, Name = {device['name']}")

def insert_services(db, services):
    collection = db['services']
    for service in services:
            collection.insert_one(service)




