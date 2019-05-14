
#Importing can be similarly viewed as calling or declaring a foreign entity,
import RPi.GPIO as GPIO                  #Importing the Raspberry GPIO pins controller Module
import time                              #Importing the python time module

in1 = 16                                 #See matriculation of the Raspberry Pi Pins for correct connection
in2 = 18                                 #This are the pin outlet to connect to!

GPIO.setmode(GPIO.BOARD)
GPIO.setup(in1, GPIO.OUT)
GPIO.setup(in2, GPIO.OUT)

GPIO.output(in1, False)                  #A "False" State translate into No Power
GPIO.output(in2, False)                  #A "True" State translates into Power passing through

try:
    while True:
      for x in range(5):                 #From the range of 0 to 5; iteratively count
            GPIO.output(in1, True)
            time.sleep(0.1)              #Code Execution Halts For Variable declared in the Brakets"()"; in this case it's 0.1 seconds
            GPIO.output(in1, False)
            GPIO.output(in2, True)
            time.sleep(0.1)                 
            GPIO.output(in2, False)
      
      GPIO.output(in1,True)
      GPIO.output(in2,True)

      for x in range(4):                 #From the range of 0 to 4; iteratively count
            GPIO.output(in1, True)
            time.sleep(0.05)
            GPIO.output(in1, False)
            time.sleep(0.05)
      GPIO.output(in1,True)

      for x in range(4):                 #From the range of 0 to 4; iteratively count
            GPIO.output(in2, True)
            time.sleep(0.05)
            GPIO.output(in2, False)
            time.sleep(0.05)
      GPIO.output(in2,True)



except KeyboardInterrupt:
    GPIO.cleanup()
