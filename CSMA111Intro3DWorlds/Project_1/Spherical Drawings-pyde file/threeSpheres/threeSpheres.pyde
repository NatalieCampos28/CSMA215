#Campos_Natalia_01.25.21
#Drawings using lines and triangles to form three views of one sphere

import os
from PolyLine import PolyLine
from TrigCirc import TrigCirc
from Triangle import Triangle
from PointOnLine import PointOnLine

#Variables
Width =1000
Height =1000
centerX = Width/2
centerY = Height/2
radius = Width/10
movie = False

#Global Variables
horAngle = 0
verAngle = 0
scalar = 0
scalar2 = .5

#Lists for polyLine coordinates
X1 = []
Y1 = []
Z1 = []

#obl list
xObl = []
yObl = []
zObl = []

#top list
xTop = []
yTop = []
zTop = []

#front list
xFront = []
yFront = []
zFront = []

#rotates the sphere
rotation = 0
rotation2 = 0

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
    #instantiates global variables to allow function draw to have it in its scope
    global centerX,centerY, radius, X1, Y1, Z1, rotation, rotation2, xObl, yObl, zObl, xTop, yTop, zTop, xFront, yFront, zFront, scalar, scalar2
    
    #change color by scalar from PointOnLine
    scalar+=.0009
    scalar2-=.0002
    
    #color variable instantiated by PointOnLine to change sphere 
    color1 = PointOnLine(255,0,0,0,80,255,scalar)
    coLor = color(color1[0], color1[1], color1[2])
    
    #color variable instantiated by PointOnLine to change background
    color2 = PointOnLine(200,80,255,230,95,0,scalar2)
    colBack = color(color2[0], color2[1], color2[2])
    background(colBack)
    
    #prints to console
    print(color1)
    print(color2)
    
    #rotations
    rotation+=4
    rotation2+= 8
    #rotateX(radians(45))
    
    #draw heights of spheres
    cyObl = -Height/3.25
    cyTop = 0
    cyFront = Height/3.25
    
    #angles
    horAngle = -15
    verAngle = -.05
    
    #move to center
    translate(centerX, centerY)
    
    #First cycle
    #TrigCirc(HorAngle, VerAngle, Radius, CenterX, CenterY, CenterZ, Rotation, Oreint)
    noStroke()
    #draw obl sphere
    circPts = TrigCirc(horAngle*.5, verAngle, radius, 0, cyObl, 0, rotation, "Oblique")
    #draw top sphere
    circPts2 = TrigCirc(horAngle*.5, verAngle, radius, 0, cyTop, 0, rotation, "Top")
    #draw front sphere
    circPts3 = TrigCirc(horAngle*1.5, verAngle, radius, 0, cyFront, 0, rotation, "Front")
    
    #obl
    x= circPts[0]
    y= circPts[1]
    z= circPts[2]
    
    #top
    xT= circPts2[0]
    yT= circPts2[1]
    zT= circPts2[2]
    
    #front
    xF= circPts3[0]
    yF= circPts3[1]
    zF= circPts3[2]
    
    #second cycle
    #TrigCirc(HorAngle, VerAngle, Radius, CenterX, CenterY, CenterZ, Rotation, Oreint)
    noStroke()
    #draw obl sphere
    circPtsOut = TrigCirc(-horAngle, verAngle, radius/3, x, y, z, rotation2, "Oblique")
     #draw top sphere
    circPtsOut2 = TrigCirc(-horAngle, verAngle, radius/3, xT, yT, zT, rotation2, "Top")
     #draw front sphere
    circPtsOut3 = TrigCirc(-horAngle, verAngle, radius/3, xF, yF, zF, rotation2, "Front")
    
    #obl
    xO= circPtsOut[0]
    yO= circPtsOut[1]
    zO= circPtsOut[2]
    
    #top
    xOT= circPtsOut2[0]
    yOT= circPtsOut2[1]
    zOT= circPtsOut2[2]
    
    #front
    xOF= circPtsOut3[0]
    yOF= circPtsOut3[1]
    zOF= circPtsOut3[2]
    
    #list up obl
    xObl.append(xO)
    yObl.append(yO)
    zObl.append(zO)
    
    #list up top
    xTop.append(xOT)
    yTop.append(yOT)
    zTop.append(zOT)
    
    #list up front
    xFront.append(xOF)
    yFront.append(yOF)
    zFront.append(zOF)
    
    #create lines for obl,top,front
    stroke(coLor)
    strokeWeight(.9)
    PolyLine(xObl,yObl,zObl)
    PolyLine(xTop,yTop,zTop)
    PolyLine(xFront,yFront,zFront)

    #line that connects each sphere
    stroke(0)
    strokeWeight(.9)
    line(xO,yO,xOF,yOF)
    
    #variable to locate when the drawing has drawn full sphere
    fullSphere = degrees(circPts[4])
    
    #condition to end movie and save to its own file
    if movie == True:
        saveFrame("anim4/" + "frame" + "-####.png")
        
        
    #condition to end drawing and save image
    if abs(fullSphere) >= 180.0:
        save("images/" + str(file_name) + str(second()) + ".jpg")
        noLoop()
    
