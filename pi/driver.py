from arduino_connection import ArduinoConnection
import serial
import fish_tank
import socket
import json
import pickle
import time

ser = fish_tank.connect_arduino()
if ser is None:
    print('Unable to find serial connection')
    exit(1)
arduino = ArduinoConnection(ser)


try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(('192.168.1.53', 8001))
except socket.error:
    print('Unable to connect to server')

handshake_data = {'device' : 'smart-fish-tank',
        'accept' : True
        }

s.send(json.dumps(handshake_data).encode())

time.sleep(2)

arduino.refresh_out()

tankData = {
                'temperature-0' : float(arduino.get('temperature-sensor 0')),
                'temperature-1' : float(arduino.get('temperature-sensor 1')),
                'ph'            : float(arduino.get('ph')),
                'turbidity'     : float(arduino.get('turbidity')),
                'test'          : 0.32,
                'alarm'         : False
            }
s.send(json.dumps(tankData).encode())

# fish_tank.main()

# if __name__ in '__main__':
#     main();