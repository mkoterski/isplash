#!/usr/bin/env python
# Simple pump test script with menu
# 
# Last Update: 2020-10-06
# Modified by: Matthias Koterski
#
# Change log: 
# 
# 0.1a - Initial version. LED turns on and off every second.
#
# Pump is connected to pin XX, relais is connected to pin XX
#
################################################################################################################


# Deactivate error warnings
# GPIO.setwarnings(False)


# To discover information about your RPi:

# GPIO.RPI_INFO

# To discover the Raspberry Pi board revision:

# GPIO.RPI_INFO['P1_REVISION']

# To discover the version of RPi.GPIO:

# GPIO.VERSION





import RPi.GPIO as GPIO
import time

# import only system from os 
from os import system, name 

# Set #27 as LED pin
RelayPin = 27

# define our clear function 
def clear_screen(): 

    # for windows 
    if name == 'nt': 
        _ = system('cls') 

    # for mac and linux(here, os.name is 'posix') 
    else: 
        _ = system('clear') 
# menu
def menu():
    #setup() # calling setup() would reset the LED status to OFF
    clear_screen()
    print (50 * '-')
    print ("")
    print ("           P U M P   T E S T   0.1 \n")
    print ("Ensure that the pump is connected to XXXXXXXX\n")
    print (50 * '-')
    print ("1 - PUMP ON")
    print ("2 - PUMP OFF")
    print ("3 - Close program")
    print (50 * '-')
     
    # Get input and convert str to int
    choice = int(input('Enter your choice [1-3] : '))
     
    # Take action as per selected menu-option ###
    if choice == 1:
            print ("Pump turning on...")
            setup()
            GPIO.output(RelayPin, GPIO.LOW)
            time.sleep(3)
            menu()
    elif choice == 2:
            print ("Pump turning off...")
            setup()
            GPIO.output(RelayPin, GPIO.HIGH)
            time.sleep(3)
            menu()
    elif choice == 3:
            print ("Shutting down program...")
            clear_screen()
            destroy()
    else:    ## default ##
            print ("Invalid number. Try again...")
            time.sleep(2)
            menu()

# Define a setup function for some setup
def setup():
    # Set the GPIO modes to BOARD numbering so that the code can be easily reused
    GPIO.setmode(GPIO.BCM)
    # Set RelayPin's mode to output, 
    # and initial level to High(3.3v)
    GPIO.setup(RelayPin, GPIO.OUT, initial=GPIO.HIGH)

# Define a destroy function for clean up everything afterwards

def destroy():
    # Turn off LED
    GPIO.output(RelayPin, GPIO.HIGH)
    # Release resource
    GPIO.cleanup()                     

# If run this script directly, do:
if __name__ == '__main__':
    setup()
    try:
            menu()
    # When 'Ctrl+C' is pressed, the child program 
    # destroy() will be  executed.
    except KeyboardInterrupt:
        destroy()