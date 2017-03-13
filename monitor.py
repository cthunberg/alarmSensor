#!/usr/bin/env python

import sys
import time

import paho.mqtt.client as mqtt
import CHIP_IO.GPIO as GPIO

def motion_callback(channel):
    print("Motion on %s" % channel)

# Motion detector, 5v
GPIO.setup("XIO-P0", GPIO.IN)
GPIO.add_event_detect("XIO-P0", GPIO.FALLING)

# Clean up every exported GPIO Pin
GPIO.cleanup()
