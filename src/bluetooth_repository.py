from pymongo import MongoClient

class BluetoothRepository:
  URI = "mongodb://127.0.0.1:27017"
  DATABASE = None

  @staticmethod
  def initialize():
    client = MongoClient(BluetoothRepository.URI)
    BluetoothRepository.DATABASE = client["bluetooth"]


  @staticmethod
  def insert(collection, data):
    return BluetoothRepository.DATABASE[collection].insert(data)

  @staticmethod
  def find_one(collection, data):
    return BluetoothRepository.DATABASE[collection].find_one(data)

  @staticmethod
  def already_exits(collection, data):
    data = BluetoothRepository.DATABASE[collection].find_one(data)
    return bool(data)
