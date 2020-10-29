import RPi.GPIO as gpio #importing package
import time #importing package


def init():
    gpio.setmode(gpio.BOARD)
    gpio.setup(7, gpio.OUT)
    gpio.setup(11, gpio.OUT)
    gpio.setup(13, gpio.OUT)
    gpio.setup(15, gpio.OUT)
    gpio.output(7, True)
    gpio.output(11, True)

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
