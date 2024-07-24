''' Test Dual dispaly of Main and common board '''
#import required libraries

from machine import Pin, SPI
import random
import gc9a01
import vga1_bold_16x32 as font
from time import sleep

spi0 = SPI(0, baudrate=40000000, sck=Pin(18), mosi=Pin(19)) # Main (RP2040) board Display SPI pins
spi1 = SPI(1, baudrate=40000000, sck=Pin(10), mosi=Pin(11))	# Common base board display SPI pins

# Define TFT displays with different CS pins
tft0 = gc9a01.GC9A01(spi0, 240, 240, reset=Pin(16, Pin.OUT), cs=Pin(17, Pin.OUT), dc=Pin(6, Pin.OUT), backlight=Pin(7, Pin.OUT), rotation=0)
tft1 = gc9a01.GC9A01(spi1, 240, 240, reset=Pin(12, Pin.OUT), cs=Pin(13, Pin.OUT), dc=Pin(14, Pin.OUT), backlight=Pin(15, Pin.OUT), rotation=0)

tft0.init()
tft1.init()

def clear_text(tft, x, y, width, height):
  """Clears a rectangular area on the TFT display."""
  tft.fill(bg, x, y, width, height)

tft0.fill(0)
tft1.fill(0)


while True:
  for rotation in range(4):
    fg = gc9a01.color565(
        random.getrandbits(8),
        random.getrandbits(8),
        random.getrandbits(8))

    bg = gc9a01.color565(
        random.getrandbits(8),
        random.getrandbits(8),
        random.getrandbits(8))
    
    tft0.rotation(rotation)
    tft1.rotation(rotation)

    tft0.text(font, "TFT0", 50, 50, fg, bg)
    tft1.text(font, "TFT1", 40, 40, fg, bg)
    sleep(0.1)

