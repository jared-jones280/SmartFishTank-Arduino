import time
import serial

class ArduinoConnection:

    def __init__(self, serial):
        self.serial = serial

    def get(self, command):
        command = command.rstrip() + ' '
        self.serial.write(command.encode())

        while self.serial.in_waiting == 0:
            time.sleep(0.05)
        
        return self.serial.read(self.serial.in_waiting)

    def read(self, buffer_size=-1):
        in_waiting = self.serial.in_waiting
        
        if buffer_size == -1:
            buffer_size = in_waiting

        if in_waiting == 0:
            return ('', 0)
        else:
            return (self.serial.read(buffer_size), min(buffer_size, in_waiting))
