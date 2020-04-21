from arduino_connection import ArduinoConnection
import serial

def main():
    ser = serial.Serial('/dev/ttyACM0', 9600, timeout=0.050)
    serial_connection = ArduinoConnection(ser)

if __name__ in '__main__':
    main();