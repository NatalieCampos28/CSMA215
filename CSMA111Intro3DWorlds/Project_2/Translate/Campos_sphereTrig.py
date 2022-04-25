#Campos_Natalia_2.10.21
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
spheres = []

#TrigCirc(HorAngle, VerAngle, Radius, CenterX, CenterY, CenterZ, Rotation, Orient)
for i in range(1,180,1):
    
    #creates random sizes of spheres in a grid
    a = random.randint(1,20)
    pt = TrigCirc(20,.5,100,0,0,0,i,"ThreeD")
  
    #adds the spherical points
    ptList = rs.AddPoint(pt[0],pt[1],pt[2])
    spher = rs.AddSphere(ptList,a)
    spheres.append(spher)

uni = rs.BooleanUnion(spheres)

for i in uni:
    color = rs.AddMaterialToObject(i)
    rs.MaterialColor(color,(2,50,101))
    
    
#rs.CreatePreviewImage("Campos.jpg")