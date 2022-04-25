#Campos_Natalia_CSMA112_011921
#Code for micro controller
from machine import Pin
from m5stack import lcd

#variables
button = Pin(37, Pin.IN)
count = 0;
#c2 = 0;

lcd.clear()

#press the big button and code will cause a change
while True:
    if button.value() == 0:
        print("button is pressed")
        #prints on lcd screen
        lcd.text(10, 10, "Welcome!")
        lcd.text(10, 20, "Press the button to change color of the ball.")
        count+=1
        if count == 1:
            lcd.clear()
            #create moving ball
            lcd.fillCircle(40, 100, 10,0xFFFFFF)
        if count == 2:
            lcd.fillCircle(40, 100, 10,0xFF0000)
        if count == 3:
            lcd.fillCircle(40, 100, 10,0x00FF00)
        if count == 4:
            lcd.fillCircle(40, 100, 10,0x0000FF)
            count = 0
    else:
        print("button is not being pressed")

