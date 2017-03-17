#!/usr/bin/env python

import sys
import time

import ConfigParser

import paho.mqtt.client as mqtt
import CHIP_IO.GPIO as GPIO

## Alarm panel PINs
# Window Alarm
W_PIN = 
# Door Pin
D_PIN =
# Motion Pin
M_PIN =


def motion_callback(channel):
    print("Motion on %s" % channel)
    # Out to alarm panel
    GPIO.output(M_PIN, GPIO.HIGH)
    time.sleep(0.5)
    GPIO.output(M_PIN, GPIO.LOW)

def window_callback(channel):
    print("Window is open on %s" % channel)
    # Out to alarm Panel
    GPIO.output(W_PIN, GPIO.HIGH)
    time.sleep(0.5)
    GPIO.output(W_PIN, GPIO.LOW)

def door_callback(channel):
    print("Door is open on %s" % channel)
    # Out to alarm Panel
    GPIO.output(D_PIN, GPIO.HIGH)
    time.sleep(0.5)
    GPIO.output(D_PIN, GPIO.LOW)


## Setup GPIOs
GPIO.toggle_debug()

try: 
    # Window Sensors
    GPIO.setup("CSID0", GPIO.OUT)
    # Door Sensors
    GPIO.setup("CSID0", GPIO.OUT)
    # Motion Sensors
    GPIO.setup("CSID0", GPIO.OUT)

    # Input
    GPIO.setup("XIO-P0", GPIO.IN)

    # Motion detector, 5v
    GPIO.setup("XIO-P0", GPIO.IN)
    GPIO.add_event_detect("XIO-P0", GPIO.FALLING)
    GPIO.add_event_callback("XIO-P0", motion_callback)

except:
    print "Error"

# Clean up every exported GPIO Pin
finally:
    GPIO.cleanup()
