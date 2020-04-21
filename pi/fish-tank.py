import time
from adafruit_motorkit import MotorKit
from adafruit_motor import stepper
import serial



def serial_test():
    ser = serial.Serial('/dev/ttyACM0')

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