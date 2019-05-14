import serial, time
arduino = serial.Serial('COM3', 9600,timeout=.1)   
time.sleep(2)

def envia():         
    arduino.write(b'0')      
    rawString = arduino.readline()    
    print(rawString.decode('ascii',errors='replace'),end='')    
    return rawString.decode('ascii',errors='replace').replace('\n','').replace('\r','')

def recibe():            
    arduino.write(b'1')        
    rawString = arduino.readline()
    print(rawString.decode('ascii',errors='replace'),end='')    
    return rawString.decode('ascii',errors='replace').replace('\n','').replace('\r','')


def close():
    arduino.close()    