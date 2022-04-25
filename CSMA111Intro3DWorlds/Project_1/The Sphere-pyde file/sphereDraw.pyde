#Campos_Natalia_01.15.21
#Drawings using lines, movements of triangles and circles to create a 3D view of a sphere

import os
from PolyLine import PolyLine
from TrigCirc import TrigCirc
from Triangle import Triangle
from PointOnLine import PointOnLine

#Variables
Width = 1000
Height = 1000
centerX = Width/2
centerY = Height/2
radius = Width
movie = False

#Global Variables
horAngle = 0
scalar = .5
scalar2 =.5

#Lists for polyLine coordinates
X1 = []
Y1 = []
Z1 = []

#rotates the sphere
rotation = 0

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
    global centerX, centerY, radius, X1, Y1, Z1, rotation, scalar, scalar2

    #change color by scalar from PointOnLine
    scalar+=.0005
    scalar2-=.0005
    
    #color variable instantiated by PointOnLine to change sphere 
    color1 = PointOnLine(0,0,255,255,0,0,scalar)
    coLor = color(color1[0], color1[1], color1[2])
    
    #color variable instantiated by PointOnLine to change background
    color2 = PointOnLine(255,0,0,0,0,255,scalar2)
    colBack = color(color2[0], color2[1], color2[2])
    background(colBack)
    
    #prints to console
    print(color1)
    print(color2)
    
    #move to center
    translate(centerX, centerY)
    
    #rotations
    rotation+=2
    #rotateX(radians(45))
    
    #draw sphere
    #TrigCirc(HorAngle, VerAngle, Radius, CenterX, CenterY, CenterZ, Rotation, Oreint)
    stroke(coLor)
    strokeWeight(3)
    circPts = TrigCirc(90, 2, radius/3, 0, 5, 0, rotation, "Oblique")
    
    x= circPts[0]
    y= circPts[1]
    z= circPts[2]
    
    #draw polyline
    PolyLine(X1,Y1,Z1)
    
    #draw triangle
    #Triangle(CenterX, CenterY, CenterZ, RadiusX, RadiusY, RadiusZ):
    stroke(0)
    strokeWeight(.8)
    Triangle(0, 0, 0, x, y, z)
    
     #condition to end movie and save to its own file
    if movie == True:
        saveFrame("anim4/" + "frame" + "-####.png")
    
    #condition to end drawing and save image
    if rotation >= 1800:
            save("images/" + str(file_name) + str(second()) + ".jpg")
            
            noLoop()
    
