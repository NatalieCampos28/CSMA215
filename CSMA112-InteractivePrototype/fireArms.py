#CSMA112 03/02/2021
#Natalie Campos
#Fire Arms code

#imports
from machine import Pin, PWM
import time
import math
from machine import ADC, Pin

#pin assignments
analogPin = ADC(Pin(36))
analogPin.atten(ADC.ATTN_11DB)

buzzer = Pin(0, Pin.OUT)

#variables
servo = PWM(Pin(26))       # wire up the yellow wire of your servo motor to pin G26
servo.freq(50)             # common servos want updates 50 times a second
pos = 13                   #assigns position for rotation
on = False
#run code
while True:
    flex = analogPin.read()
    buzzer.on()

    #if flex sensor is greater than 124 rotate servo motor
    if flex >= 1000:

        servo.resume()          #continue
        print("Start")            #check code run
        servo.duty(pos)        # tells the servo to move to one position (angle)
        buzzer.off()
        time.sleep_ms(100)    #shorter run
        servo.pause()           #pause
        print("Done")            #check code run

    print("Run")
    time.sleep_ms(1000)


#output = 3.3 V
#call off method
