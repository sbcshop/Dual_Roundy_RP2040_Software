''' Onboard SDcard operation Demo'''
# import required libraries
from machine import Pin, SPI
from dualdisplay import SDCard
from time import sleep
import os

#function performs detection, write and read operation on micro SDcard
def sdtest(data):
    try:
        spi=SPI(0,sck=Pin(2),mosi=Pin(3),miso=Pin(4)) #define and configure sdcard SPI interfacing
        sd=SDCard(spi,Pin(5)) # SDCard(arg1, arg2) => arg1 : SPI, arg2 : CS
        vfs = os.VfsFat(sd) 
        os.mount(vfs, "/fc")   # mount SD card
        print("Filesystem check")
        print(os.listdir("/fc")) # list directories present in sdcard

        fn = "/fc/File.txt"		#create file with suitable name
        print()
        print("Single block read/write")
        with open(fn, "a") as f:
            n = f.write(data)		#write data to file
            print(n, "bytes written") 

        with open(fn, "r") as f:
            result2 = f.read()		#read data from file
            print(len(result2), "bytes read\n")
            print("Data written on File:")
            print(result2)
        
        print("SDcard R/W Ok!")
        os.umount("/fc")
        
    except OSError as e:
        print("OS Error: ", e)
        

sdtest('Hello!!\n')
sleep(2)





