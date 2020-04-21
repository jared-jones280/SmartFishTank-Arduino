import time

class ArduinoConnection:

    def __init__(self, serial):
        self.serial = serial

    def get(self, command):
        self.serial.write(command.encode())

        while serial.in_waiting == 0:
            time.sleep(0.05)
        
        return self.serial.readLine()