#!/usr/bin/env python

# All work is under Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License.
# Be free to repost this code but say it was originally from me.
# this is made to work with led strip lights that use pwm but can be easily changed to work with other things.

#pretty obvious, but you'll want these dependencies to be installed for this script to work
import RPi.GPIO as GPIO
import time
import requests
import os

def cls():
    os.system(['clear','cls'][os.name == 'nt'])

DEBUG = 1

#this defines the pins for what colour  
RED = 23
GREEN = 24
BLUE = 25

GPIO.setmode(GPIO.BCM)
GPIO.setup(RED, GPIO.OUT)
GPIO.setup(GREEN, GPIO.OUT)
GPIO.setup(BLUE, GPIO.OUT)

#replace the http://YourWebsite.com/test.php with where your test.php is located.


response = requests.get('http://YourWebsite.com/test.php')

while response.text != 'exit':
    response = requests.get('http://YourWebsite.com/test.php')

#This says red is the first digit green is the second and blue is the last 
    colrs = response.text
    r = colrs[0]
    g = colrs[1]
    b = colrs[2]

    cls()

    if response.text == 'exit':
        print (colrs)
    else:
        print ("R" + r + ", "),
        print ("G" + g + ", "),
        print ("B" + b)
        print

# This says if the number is 1 then the the light is on else if it is 0 the light is off.
    if r == '1':
        GPIO.output(RED,True)
    else:
        GPIO.output(RED,False)
    if g  == '1':
        GPIO.output(GREEN,True)
    else:
        GPIO.output(GREEN,False)
    if b  == '1':
        GPIO.output(BLUE,True)
    else:
        GPIO.output(BLUE,False)
		

#This can be removed but this time is to stop the web server from being overloaded with requests.
    time.sleep(0.15)