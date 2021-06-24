import serial
import time
import numpy as np

# Configuration file name
configFileName = '1443config.cfg'



def serialConfig(configFileName):
        
    # Linux
    #CLIport = serial.Serial('/dev/ttyACM0', 115200)
    #Dataport = serial.Serial('/dev/ttyACM1', 921600)
    
    # Windows
    CLIport = serial.Serial('COM17', 115200)
    Dataport = serial.Serial('COM18', 921600)

    # Download config from file
    config = [line.rstrip('\r\n') for line in open(configFileName)]
    for i in config:
        CLIport.write((i+'\n').encode())
        print(i)
        time.sleep(0.01)
    
    #CLIport.write(('sensorStop\n').encode())
    CLIport.close()
    Dataport.close()    
    return

serialConfig(configFileName)
    





