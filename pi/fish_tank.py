import time, socket, json, pickle
import os
from adafruit_motorkit import MotorKit
from adafruit_motor import stepper
import serial

from arduino_connection import ArduinoConnection

URL = '192.168.1.53'
PORT = 8001

def main():

    # socket connection
    connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # connection.connect(('pi.cmasterx.com', 8001))
    connection.connect(('192.168.1.53', 8001))
   
    # arduino connection
    arduino = ArduinoConnection(connect_arduino())

    # establish handshake
    handshake_data = {'device' : 'smart-fish-tank',
        'accept' : True
        }

    connection.send(json.dumps(handshake_data).encode())


    # stepper
    kit = MotorKit()
    stepper = kit.stepper1

    while True:
        try:
            #send data
            tankData = {
                'temperature-0' : arduino.get('temperature-sensor 0'),
                'temperature-1' : arduino.get('temperature-sensor 1'),
                'ph'            : arduino.get('ph'),
                'turbidity'     : arduino.get('turbidity'),
                'alarm'         : False
            }
            
            dump = json.dumps(tankData).encode()
            print("length: {}".format(dump))
            
            connection.send(json.dumps(tankData).encode())
            
        except:
            # re-establish connection to server
            connection.close()
            connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            connection.connect((URL, PORT))

        time.sleep(1)


def connect_arduino():
    path = '/dev/ttyACM'
    
    for i in range(5):

        if os.path.exists('{}{}'.format(path, i)):
            try:
                return serial.Serial('{}{}'.format(path, i), 9600, timeout=0.050)
            except serial.serialutil.SerialException:
                pass
        
    return None

# for i in range(20):
#     kit.stepper1.onestep(style=stepper.SINGLE)
#     time.sleep(0.5)
# time.sleep(0.5)
# kit.stepper1.release()

def test(*args):
    print(args)

if __name__ == '__main__':
    test()
    main()
