import RPi.GPIO as gpio #importing package
import time #importing package


def init():
    gpio.setmode(gpio.BOARD)
    gpio.setup(7, gpio.OUT) #initializing pin in1 of motor driver
    gpio.setup(11, gpio.OUT) #initializing pin in2 of motor driver
    gpio.setup(13, gpio.OUT) #initializing pin in3 of motor driver
    gpio.setup(15, gpio.OUT) #initializing pin in4 of motor driver
    gpio.output(7, True) #setting pin 7 to True
    gpio.output(11, True) #setting pin 11 to True

def forward(tf):
    gpio.output(13, True)
    gpio.output(15, False)
    time.sleep(tf)

def reverse(tf):
    gpio.output(13, False)
    gpio.output(15, True)
    time.sleep(tf)


init()
forward(0.5)
reverse(0.5)

gpio.cleanup()
