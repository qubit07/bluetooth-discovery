from bluetooth_service import BluetoothService
import time


if __name__ == '__main__':
    service = BluetoothService()
    while True:
        service.find_devs()
        time.sleep(5)
