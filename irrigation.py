#Python is High End language built oer c


import RPi.GPIO as GPIO    #Importing Raspberry Pi GPIO pins controll module
import time                #Importing timer module


GPIO.setmode(GPIO.BOARD)   # Set Gpio pins tag in a board setting.
GPIO.setwarnings(False)    # Turn off all warnings of sf.


#Assigning the sensor a respective pin number
#Open Terminal in Rasperry Pi; Type Pinout to inform yourself on the different pins.
moisture_sensor = 7               #the moisture pin is given 7
rain_sensor = 10                  #the rain sensor is given 10

                           #Assigning the Power Relay Module respective pin number
water_pump = 5                
                


GPIO.setup(moisture_sensor, GPIO.IN)      #
GPIO.setup(rain_sensor, GPIO.IN)          #
GPIO.setup(water_pump, GPIO.OUT)      #      #



Raining_Status = False                    # Set initial data as false

GPIO.output(water_pump, False)        #
        #



def pump_actuator(moisture):                           #
    if GPIO.input(moisture_sensor) == 1:                                 #
        print('Soil is Dry!')
        if GPIO.input(rain_sensor) == 0:
            print("it is raining tho!, so i won't pump water")
        elif GPIO.input(rain_sensor) == 1:
            print('Soil is dry but not raining')
            GPIO.output(water_pump, True)
    elif GPIO.input(moisture_sensor) == 0:
        print('---------------------------')
        print('Enough Water is in the soil')
        print('---------------------------')
        GPIO.output(water_pump, False)
        


GPIO.add_event_detect(moisture_sensor, GPIO.BOTH, bouncetime=100)
GPIO.add_event_callback(moisture_sensor, callback=pump_actuator)


    
