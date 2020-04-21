import time
from adafruit_motorkit import MotorKit
from adafruit_motor import stepper

kit = MotorKit()

kit.stepper1.release()

time.sleep(5)

for i in range(20):
    kit.stepper1.onestep(style=stepper.SINGLE)
    time.sleep(0.5)
time.sleep(0.5)
kit.stepper1.release()