import RPi.GPIO as GPIO
import pygame.mixer
import time
import signal
import os, sys
import subprocess

def activeSetup():
    global active
    active=0
    print("Currently Not Active")
def activeState():
    global active
    if active==1:
        active=0
        GPIO.output(7,GPIO.LOW)
        print("Currently Not Active")
    elif active==0:
        print ("Activating in 5 seconds")
        for x in range(0,5):
            GPIO.output(7,GPIO.HIGH)
            time.sleep(0.5)
            GPIO.output(7,GPIO.LOW)
            time.sleep(0.5)
        active=1
        GPIO.output(7,GPIO.HIGH)
        print("Currently Active")
    else: return
def watchDoor():
    global playing
    playing = False
    
    omxprocess=""
    while True:
        if active==1 and GPIO.input(15)==1 and playing==False:
            playing=True
            print("Should play music")
            omxprocess = subprocess.Popen(['omxplayer',"Oops-crop.mp3"],stdin=subprocess.PIPE,stdout=None,stderr=None,bufsize=0)
        if GPIO.input(13)==1:
            print("Stop button pressed: Exiting")
            omxprocess.stdin.write(b'q')
            break
        if GPIO.input(11)==1:
            activeState()
            time.sleep(0.5)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(7, GPIO.OUT,initial=GPIO.LOW)
GPIO.setup(11,GPIO.IN)
GPIO.setup(13,GPIO.IN)
GPIO.setup(15,GPIO.IN)

activeSetup()

while True:
    if(GPIO.input(13)==1):
        print("Stop button pressed: Exiting")
        break
    if(GPIO.input(11)==1):
        activeState()
        time.sleep(0.5)
    if(active==1):
        watchDoor()
        break
GPIO.cleanup()

