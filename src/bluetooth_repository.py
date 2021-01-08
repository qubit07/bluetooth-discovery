from pymongo import MongoClient

class BluetoothRepository:
  URI = "http://localhost:27017"
  DATABASE = None

  @staticmethod
  def initialize():
    client = MongoClient(BluetoothRepository.URI)
    BluetoothRepository.DATABASE = client["bluetooth"]


  @staticmethod
  def insert(collection, data):
    return BluetoothRepository.DATABASE[collection].insert(data)
