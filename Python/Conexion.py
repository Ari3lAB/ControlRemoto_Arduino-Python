import serial
import time

# Iniciar la conexion desde un método para que no se inicie desde que se implementa la clase en la interfaz!!!!!!
arduino = serial.Serial('COM3', 9600, timeout=.5)
time.sleep(2)


def temp():
    arduino.write(b'0')
    rawString = arduino.readline()
    time.sleep(1.5)
    rawString = rawString.decode('ascii', errors='replace').replace(
        '\n', '').replace('\r', '')
    rawString = rawString[:-3]    
    return rawString


def humid():
    arduino.write(b'1')
    rawString = arduino.readline()
    time.sleep(1.5)    
    rawString = rawString.decode('ascii', errors='replace').replace(
        '\n', '').replace('\r', '')
    rawString = rawString[:-3]    
    return rawString


def setLed():
    arduino.write(b'2')
    time.sleep(1.5)
    rawString = arduino.readline()       
    rawString = rawString.decode('ascii', errors='replace').replace(
        '\n', '').replace('\r', '')
    return rawString

def checkLed():
    arduino.write(b'3')
    time.sleep(1.5)    
    rawString = arduino.readline()
    rawString = rawString.decode('ascii', errors='replace').replace(
        '\n', '').replace('\r', '')    
    return rawString