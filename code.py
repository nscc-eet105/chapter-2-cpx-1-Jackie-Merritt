#First Project
#Blink Leds

from adafruit_circuitplayground import cp
import time

while True:
     cp.red_led = True
     time.sleep(.5)
     cp.red_led = False
     time.sleep(.5)
     #Neopixel Time!!
     cp.pixels[0] = (0, 100, 100) #
     time.sleep(.5)
     cp.pixels[0] = (0, 0, 0) #all off
     time.sleep(.5)
     #Second Neopixel
     cp.pixels[1] = (128, 0, 128) #Purple
     time.sleep(.5)
     cp.pixels[1] = (0, 0, 0) #all off
     time.sleep(.5)
