import time
import serial

class ArduinoConnection:

    def __init__(self, serial):
        self.serial = serial

    def get(self, command, nice=True, timeout=0.5, wait=0.5):
        command = command.rstrip() + ' '
        self.serial.write(command.encode())

        start = time.time()
        
        while self.serial.in_waiting == 0 and time.time() - start < timeout:
            time.sleep(0.05)
        
        time.sleep(wait)
        
        return clean(self.serial.read(self.serial.in_waiting).decode(), nice=nice)

    def read(self, buffer_size=-1, nice=True):
        in_waiting = self.serial.in_waiting
        
        if buffer_size == -1:
            buffer_size = in_waiting

        if in_waiting == 0:
            return ('', 0)
        else:
            return (clean(self.serial.read(buffer_size).decode(), nice=nice), min(buffer_size, in_waiting))

    def refresh_out(self):
        self.read(nice=False)

def clean(str, nice=True, decode=True):
    if str is bytes:
        str = str.decode()
    
    while nice and len(str) != 0 and (str[-1] == '\n' or str[-1] == '\r'):
        str = str[:-1]
    
    return str