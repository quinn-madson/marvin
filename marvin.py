#!/usr/bin/python
#
# marvin.py
# Nintendo Wii Remote controller for Snap
# Circuits robot.
#
# Authors : Scarlett Madson, Solomon Madson, Quinn Madson
# Date   : 02.22.2016

# Import required Python libraries
import cwiid
import time
import pygame.mixer
import RPi.GPIO as io

# Setup Raspberry Pi GPIO pins
io.setmode(io.BCM)
pins = (4,17,27,22)
for i in pins:
  io.setup(i,io.OUT)

button_delay = 0.1

print 'Hello! I\'m Marvin the Robot.'
print 'Press 1 + 2 on your Wiimote now to pair ...'
time.sleep(1)

# Connect to the Wii Remote. If it times out then quit.
try:
  wii=cwiid.Wiimote()
except RuntimeError:
  print "Error pairing Wiimote. Please try again or try a different Wiimote."
  quit()

print 'Wiimote connected...\n'
print 'Press some buttons!\n'

wii.rpt_mode = cwiid.RPT_BTN

# Startup the pygame mixer so we can play sounds.
pygame.mixer.init()

# This function stops all the motors from running when the user takes their fingers off the buttons.
def resetPins():
  #print "resetPins()"
  io.output(4, False)
  io.output(17, False)
  io.output(22, False)
  io.output(27, False)

# Read wiimote buttons
while True:

  buttons = wii.state['buttons']
  # If nothing is being pressed, reset the motor controller pins.
  if not (buttons):
    resetPins()

  # Make marvin bark like a dog
  if (buttons & cwiid.BTN_B):
    print 'Button B pressed'
    time.sleep(button_delay)
    #Play wav file
    pygame.mixer.music.load("dog_bark_x.wav")
    pygame.mixer.music.play()

  # Check if other buttons are pressed by doing a bitwise AND of the buttons number and the predefined constant for that button.
  if (buttons & cwiid.BTN_LEFT):
    print 'Left pressed'
    time.sleep(button_delay)
    # Turn on GPIO pins to activate motor controller
    io.output(17, True)
    io.output(27, True)

  if(buttons & cwiid.BTN_RIGHT):
    print 'Right pressed'
    time.sleep(button_delay)
    io.output(22, True)
    io.output(4, True)

  if (buttons & cwiid.BTN_UP):
    print 'Up pressed'
    time.sleep(button_delay)
    io.output(17, True)
    io.output(22, True)

  if (buttons & cwiid.BTN_DOWN):
    print 'Down pressed'
    time.sleep(button_delay)
    # Make the wiimote rumble so the user pays attention when moving backwards.
    wii.rumble = 1
    time.sleep(0.25)
    wii.rumble = 0
    pygame.mixer.music.load("196567__tambascot__truck-backup-beeps.wav")
    pygame.mixer.music.play()
    io.output(4, True)
    io.output(27, True)

  # Unused buttons (for now)
  if (buttons & cwiid.BTN_1):
    print 'Button 1 pressed'
    time.sleep(button_delay)

  if (buttons & cwiid.BTN_2):
    print 'Button 2 pressed'
    time.sleep(button_delay)

  if (buttons & cwiid.BTN_A):
    print 'Button A pressed'
    time.sleep(button_delay)

  if (buttons & cwiid.BTN_HOME):
    print 'Home Button pressed'
    time.sleep(button_delay)

  if (buttons & cwiid.BTN_MINUS):
    print 'Minus Button pressed'
    time.sleep(button_delay)

  if (buttons & cwiid.BTN_PLUS):
    print 'Plus Button pressed'
    time.sleep(button_delay)
