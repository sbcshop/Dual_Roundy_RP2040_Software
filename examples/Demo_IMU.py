'''
* Demo to Read accelerometer and Gyro using onboard 6D IMU Sensor
* Reading Battery RAW analog value

'''
# import required libraries
from machine import Pin,ADC
from dualdisplay import IMU
from time import sleep


V_SENSE_PIN = 27  #pin to read battery voltage
imuData = IMU()	  #create instance to read IMU data

while 1:

    batVolt= ADC(Pin(V_SENSE_PIN)) # read analog raw value for battery 
    iVal = imuData.Read_XYZ()	   # IMU read 
    
    print("ACC_X = {:+.2f}".format(iVal[0]))
    print("ACC_Y = {:+.2f}".format(iVal[1]))
    print("ACC_Z = {:+.2f}".format(iVal[2]))
    
    print("GY_X = {:+3.2f}".format(iVal[3]))
    print("GY_Y = {:+3.2f}".format(iVal[4]))
    print("GY_Z = {:+3.2f}".format(iVal[5]))
    
    voltVal = batVolt.read_u16()*3.3/65535*2
    print("Vbat = {:.2f}".format(voltVal))
    sleep(0.2) # wait for 0.2 seconds




