import time, socket, json, pickle
from adafruit_motorkit import MotorKit
from adafruit_motor import stepper
import serial

<<<<<<< HEAD
def main():
    connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    connection.connect(('pi.cmasterx.com', 8000))

    while True:
        try:
            #send data
            tankData = {
                'temperature-0': sensor_readings('temperature', {'id': 0}),
                'temperature-1': sensor_readings('temperature', {'id': 1}),
                'ph': sensor_readings('ph'),
                'turbidity': sensor_readings('turbidity'),
                'alarm' : False
            }
            
            connection.send(pickle.dumps(tankData))
            
        except:
            # re-establish connection to server
            connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            connection.connect(('pi.cmasterx.com', 8000))

                
def sensor_readings(type, args=None):

    if type == 'temperature' and 'id' in args:
        True
    else:
        False

kit = MotorKit()
=======
>>>>>>> f4aec6ac28c0bcf479324fa9a05943cbf3423dac


def serial_test():
    ser = serial.Serial('/dev/ttyACM0')

<<<<<<< HEAD
for i in range(20):
    kit.stepper1.onestep(style=stepper.SINGLE)
    time.sleep(0.5)
time.sleep(0.5)
kit.stepper1.release()

def test(*args):
    print(args)

if __name__ == '__main__':
    test()
    main()
=======
# kit = MotorKit()

# kit.stepper1.release()

# time.sleep(5)

# for i in range(20):
#     kit.stepper1.onestep(style=stepper.SINGLE)
#     time.sleep(0.5)
# time.sleep(0.5)
# kit.stepper1.release()

if __name__ == '__main__':
    main()
>>>>>>> f4aec6ac28c0bcf479324fa9a05943cbf3423dac
