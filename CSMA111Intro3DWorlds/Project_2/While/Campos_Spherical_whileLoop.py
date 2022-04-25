#Campos_Natalia_2.22.21
#The program makes an object from spherical coordinates

#imports
#updates custom mods
import Spherical
from Spherical import TrigCirc
from imp import reload
reload(Spherical)
import CaptureView
from CaptureView import GetCaptureView

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
paths = []
stop = 700
rVal1 = 1
rVal2 = 5
rVal3 = 3
horAng = 100
verAng = .06
radius = 100
height = 7

while rVal1 <= stop:
    rVal1 +=1
    rVal2 +=1
    rVal3 +=1
    
    #rs.Sleep(1000)
    
    #creates different views of the sphere
    pt1 = TrigCirc(-horAng,verAng,radius,0,0,0,rVal1,"ThreeD")
    pt2 = TrigCirc(horAng/2,verAng,radius/3,pt1[0],pt1[1],pt1[2],rVal2*2,"ThreeD")
    pt3 = TrigCirc(horAng,verAng,radius/6,pt2[0],pt2[1],pt2[2],rVal3,"ThreeD")
    
    #adds the spherical points
    ptList = rs.AddPoint(pt3[0],pt3[1],pt3[2])
    points.append(ptList)
    
#creates a polyline 
lines = rs.AddPolyline(points)
ver = rs.AddPoint(pt3[0],pt3[1],pt3[2]+height)
path = rs.AddLine(ptList,ver)
rise = rs.ExtrudeCurve(lines,path)

#outlines surfaces of object
surfSet = rs.ExplodePolysurfaces(rise)

origin = rs.AddPoint(0,0,pt3[2])

#adds points that are on surface to a path list
for i in range(len(points)):
    path = rs.AddLine(points[i],origin)
    paths.append(path)
    
#extrudes surface with points to create solids
for i in range(len(surfSet)):
    rs.ExtrudeSurface(surfSet[i],paths[i])
    
views = rs.ViewNames()

#develops a rendered view
for view in views:
    rs.ViewDisplayMode(view,'Rendered')
    

rs.ObjectPrintWidth(lines,.2)
rs.ObjectColor(lines,(255,100,100))

#show a zoomed in view right when program runs
rs.ZoomExtents()

#rs.CreatePreviewImage("Campos_forLoop1.jpg")
