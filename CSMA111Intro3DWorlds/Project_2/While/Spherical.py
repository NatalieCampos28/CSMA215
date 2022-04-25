#Draws point on circle based on sin and cos
#Natalia Campos 2.10.21

from math import radians
from math import cos
from math import sin


def TrigCirc(HorAngle, VerAngle, Radius, CenterX, CenterY, CenterZ, Rotation, Orient):
    

    #loop to create points on sphere
    for i in range(Rotation):
        
        Hor = radians(HorAngle*i)
        Ver = radians(VerAngle*i)
        
        #condidtional to draw the sphere in 3D
        if Orient == "ThreeD":
            
            #construct coordinates on the circle
            x = cos(Hor)*Radius*sin(Ver) + CenterX
            y = sin(Hor)*Radius*sin(Ver) + CenterY
            z = cos(Ver)*Radius + CenterZ
            
        #condidtional to draw the top of the sphere
        if Orient == "Top":
            
            #construct coordinates on the circle
            x = cos(Hor)*Radius*sin(Ver) + CenterX
            y = sin(Hor)*Radius*sin(Ver) + CenterY
            z = 0 + CenterZ
            
        #condidtional to draw the Front of the sphere
        if Orient == "Front":
        
            #construct coordinates on the circle
            x = cos(Hor)*Radius*sin(Ver) + CenterX
            y = cos(Ver)*Radius + CenterZ
            z = 0 + CenterY
            
        #condidtional to draw the oblique of the sphere
        if Orient == "Oblique":
            
            #construct coordinates on the circle
            x = cos(Hor)*Radius*sin(Ver) + CenterX
            y = sin(Hor)*Radius*sin(Ver) - cos(Ver)*Radius*.9 + CenterZ + CenterY
            z = 0 + CenterZ           

    return(x,y,z)
    
