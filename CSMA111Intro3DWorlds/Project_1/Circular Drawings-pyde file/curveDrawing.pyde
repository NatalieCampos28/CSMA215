#Campos_Natalia_01.15.21
#Drawings using lines, movements of triangles and circles

import os
from PolyLine import PolyLine
from TrigCirc import TrigCirc
from Triangle import Triangle

#Variables
Width   = 1000
Height  = 1000
centerX = Width/2
centerY = Height/2

radius = Width/2

#color variables
r = random(255)
g = random(255)
b = random(255)


#Global Variables
horAngle = 0
horAngle2 = 0
horAngle3 = 0

#Lists for polyLine coordinates
X1 = []
Y1 = []
Z1 = []

#gets file name
file_name = os.path.basename(__file__)

#drawing setup
def setup():
    #P3D allows three dimensions
    size(Width,Height,P3D)
    background(255)
    smooth(100)

#loop to draw
def draw():
    background(255)
    
    #instantiates global variables to allow function draw to have it in its scope
    global centerX, centerY, horAngle, horAngle2, horAngle3, radius, X1, Y1, Z1, r, g, b
    
    #variable to create video
    movie = True
    
    #move to center
    translate(centerX, centerY)
    
    #increasing and decreasing variables to create movement of circles
    horAngle += 1
    if horAngle >= 360:
        horAngle2 += -4 +1
    else:
        horAngle2 += -4
        horAngle3 += -7
        
    #find point on circle
    circPts = TrigCirc(horAngle, radius/4,radius/2, 0, 0)
    
    x= circPts[0]
    y= circPts[1]
    z= circPts[2]
    
    #find point on circle2
    circPts2 = TrigCirc(horAngle2, radius/6, radius/3, x,y)
    
    x2= circPts2[0]
    y2= circPts2[1]*2
    z2= circPts2[2]

    #find point on circle3
    circPts3 = TrigCirc(horAngle3, radius/6, radius/3, x2,y2)
    
    x3= circPts3[0]
    y3= circPts3[1]/4
    z3= circPts3[2]
    
    #append coordinates to list
    X1.append(x3)
    Y1.append(y3)
    Z1.append(3)
    
    #Movement of triangles
    stroke(50)
    strokeWeight(.7)
    rotation1 = Triangle(0,0,x,y)
    rotation2 = Triangle(x,y,x2,y2)
    rotation3 = Triangle(x2,y2,x3,y3)
    
    #writes coordinates as circle draws
    textSize(20)
    fill(0)
    text(str(int(horAngle/360)),x,y)
    
    #draw polyline
    stroke(r,g,b)
    strokeWeight(4)
    PolyLine(X1,Y1,Z1)
    
    #condition to end movie and save to its own file
    if movie == True:
        saveFrame("anim4/" + "frame" + "-####.png")
    
    #condition to end drawing and save image
    if horAngle >= 720+2:
            save("images/" + str(file_name) + str(second()) + ".jpg")
            
            noLoop()
    
