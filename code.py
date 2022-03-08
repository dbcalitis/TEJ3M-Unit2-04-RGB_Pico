"""
LED example for Pico. Blinks external LED on and off.

REQUIRED HARDWARE:
* LED on pin GP14.
"""

# Created by: Daria Bernice Calitis
# Created on: Feb 2022

import time
import board
import digitalio


red_light = digitalio.DigitalInOut(board.GP13)
red_light.direction = digitalio.Direction.OUTPUT
red_light.value = False

green_light = digitalio.DigitalInOut(board.GP11)
green_light.direction = digitalio.Direction.OUTPUT
green_light.value = False

blue_light = digitalio.DigitalInOut(board.GP12)
blue_light.direction = digitalio.Direction.OUTPUT
blue_light.value = False

while True:
    red_light.value = True
    green_light.value = False
    blue_light.value = False
    time.sleep(1)
    
    red_light.value = False
    green_light.value = True
    blue_light.value = False
    time.sleep(1)
    
    red_light.value = False
    green_light.value = False
    blue_light.value = True
    time.sleep(1)
    
    red_light.value = True
    green_light.value = True
    blue_light.value = False
    time.sleep(1)
    
    red_light.value = True
    green_light.value = False
    blue_light.value = True
    time.sleep(1)
    
    red_light.value = False
    green_light.value = True
    blue_light.value = True
    time.sleep(1)
    
    red_light.value = True
    green_light.value = True
    blue_light.value = True
    time.sleep(1)
