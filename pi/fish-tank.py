import time, socket, json, pickle, datetime, queue, threading
from adafruit_motorkit import MotorKit
from adafruit_motor import stepper
import serial

def main(q1):
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
            msg = connection.recvmsg

            if (msg == "feed"):
                q1.put(msg)
            
        except:
            # re-establish connection to server
            connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            connection.connect(('pi.cmasterx.com', 8000))

def feeder_thread(q1):
    kit = MotorKit()

    while (True):
        if not q1.empty():
            msg = q1.get()
            if (msg == "feed"):
                for i in range(50):
                    kit.stepper1.onestep(style=stepper.DOUBLE)
                    time.sleep(0.1)

                kit.stepper1.release()
        
        time.sleep(0.01)
    

def sensor_readings(type, args=None):

    if type == 'temperature' and 'id' in args:
        True
    else:
        False


def serial_test():
    ser = serial.Serial('/dev/ttyACM0', 9600, timeout=0.050)


if __name__ == '__main__':
    q1 = queue.Queue()
    t1 = threading.Thread(target=feeder_thread, args=(q1,), daemon=True)
    t1.start()
    main(q1)
