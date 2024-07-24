''' Demo code to Play with onboard RGB LED and User Buttons '''

# Import required libraries 
from dualdisplay import RGBLED, BUTTON
from time import sleep

rgbmatrix = RGBLED()
button1 = BUTTON(1)
button2 = BUTTON(2) 
button3 = BUTTON(3)

# Control all matrix LEDs at once with a specified color and brightness
r, g, b = 0, 150, 200  # Set the RGB color values,  0-254 accepted for each 
rgbmatrix.on(color=(r,g,b) , brightness=0.02)  # Turn on the LEDs with the specified color and brightness
sleep(0.5)  # Wait for 0.5 seconds
rgbmatrix.off()  # Turn off all LEDs
sleep(0.5)  

'''
# Control individual LEDs
rgbmatrix.pixelon(0) # Turn on RGB LED at position 1
sleep(0.5)
rgbmatrix.pixeloff(0) # Turn off RGB LED at position 1

rgbmatrix.pixelon(3, brightness=0.02)  # 4th RGB with specified brightness
sleep(1)  
rgbmatrix.pixeloff(3)  # Turn off
sleep(1)  # Wait for 1 seconds
'''
while 1:
    # read button status
    val1 = button1.read()	
    val2 = button2.read()
    val3 = button3.read()
    
    print(f"Bt1 = {val1}, Bt2 = {val2}, Bt3 = {val3}")
    
    if val1 == 0:  # check if button pressed, HIGH - normally, LOW - when pressed
        print("Button1 Pressed")
        rgbmatrix.pixelon(3, color=(150, 0, 0), brightness=0.8)
        sleep(0.2)
        
    if val2 == 0:
        print("Button2 Pressed")
        rgbmatrix.pixelon(2, color=(0, 150, 0), brightness=0.8)
        sleep(0.2)
   
    if val3 == 0:
        print("Button3 Pressed")
        rgbmatrix.pixelon(1, color=(0, 0, 150), brightness=0.8)
        rgbmatrix.pixelon(0, color=(0, 0, 150), brightness=0.8)
        sleep(0.2)
        
    rgbmatrix.pixeloff(0)
    rgbmatrix.pixeloff(1)
    rgbmatrix.pixeloff(2)
    rgbmatrix.pixeloff(3) 
    sleep(0.2)