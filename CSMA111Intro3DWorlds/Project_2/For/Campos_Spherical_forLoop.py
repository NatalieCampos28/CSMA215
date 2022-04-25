
#Campos_Natalia_2.17.21
#The program makes an object from spherical coordinates

#imports
#updates custom mods
import Spherical
from Spherical import TrigCirc
from imp import reload
reload(Spherical)

#imports libraries
import rhinoscriptsyntax as rs
import math
import random

#deletes all objects to refresh
delSet = rs.AllObjects(True)
rs.DeleteObjects(delSet)

#variables
#points[] array creates list of points from sphere
points = []
stop = 720
rVal1 = 3
rVal2 = 7
rVal3 = 11
horAng = 1000
verAng = .05
radius = 100
height = 7

#TrigCirc(HorAngle, VerAngle, Radius, CenterX, CenterY, CenterZ, Rotation, Orient)
for i in range(1,360,1):
    
    #initiates rotations for each points lists according to the angle/view listed
    rot1 = rVal1*i
    rot2 = rVal2*i
    rot3 = rVal3*i
    
    #creates different views of the sphere
    pt1 = TrigCirc(-horAng,verAng,radius,0,0,0,rot1,"ThreeD")
    pt2 = TrigCirc(horAng/2,verAng,radius/4,pt1[0],pt1[1],pt1[2],rot2,"ThreeD")
    pt3 = TrigCirc(horAng,verAng,radius/8,pt2[0],pt2[1],pt2[2],rot3,"ThreeD")
    
    #adds the spherical points
    ptList = rs.AddPoint(pt3[0],pt3[1],pt3[2])
    points.append(ptList)
    

#creates a polyline 
lines = rs.AddPolyline(points)
ver = rs.AddPoint(pt3[0],pt3[1],pt3[2]+height)
path = rs.AddLine(ptList,ver)
rise = rs.ExtrudeCurve(lines,path)

#show a zoomed in view right when program runs
rs.ZoomExtents()

#rs.CreatePreviewImage("Campos_forLoop1.jpg")