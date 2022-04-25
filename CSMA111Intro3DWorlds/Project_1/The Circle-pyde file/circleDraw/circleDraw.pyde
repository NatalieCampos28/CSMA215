#Campos_Natalia_CSMA111_01.13.21
#draws a circle demonstrating coordinates 

#imports
import os
from PolyLine import PolyLine

#Variables
Width   = 1000
Height  = 1000
centerX = Width/2
centerY = Height/2

radius = Width/3

#color variables
r = random(255)
g = random(255)
b = random(255)

#Global Variables
horAngle = 0
verAngle = 0

#lists to store coordinates
X1 = []
Y1 = []
Z1 = []

#file to store this program in
file_name = os.path.basename(__file__)

#sets up canvas
def setup():
    #drawing setup
    size(Width,Height,P3D)
    background(255)
    smooth(100)

#draws using a loop
def draw():
    background(255)
    
    #instantiates global variables to allow function draw to have it in its scope
    global centerX, centerY, horAngle, verAngle, radius,X1,Y1,Z1, r, g, b
    
    #updates horiz angle
    horAngle += radians(1)
    
    #move drawing to center
    translate(centerX,centerY)
    
    #construct coordinates on the circle
    x = cos(horAngle)* radius 
    y = sin(horAngle)* radius 
    z = 0
    
    #append coordinates to list
    X1.append(x)
    Y1.append(y)
    Z1.append(z)
    
    #draw triangle
    stroke(100)
    strokeWeight(.7)
    rad = line(0,0,x,y)
    xLine =  line(0,0,x,0)
    yLine =  line(x,0,x,y)
    
    #writes coordinates as circle draws
    textSize(20)
    fill(0)
    text(str((x,y)),x,y)
    
    
    #draw polyline
    stroke(r,g,g)
    strokeWeight(4)
    PolyLine(X1,Y1,Z1)
    
    #condition to end drawing and save image
    if horAngle >= radians(360):
            save("images/" + str(file_name) + str(second()) + ".jpg" ) 
        
            noLoop()
    
