import numpy as np
import math
from random import randint
import main



##crea el mundom, una matriz de las dimensiones width y height
def createWorld(width,height):
    world = np.zeros((width,height))
    return world
##genera los puntos de un circulo
def points_in_circle_np(radius, x0=0, y0=0, ):
    x_ = np.arange(x0 - radius - 1, x0 + radius + 1, dtype=int)
    y_ = np.arange(y0 - radius - 1, y0 + radius + 1, dtype=int)
    x, y = np.where((x_[:,np.newaxis] - x0)**2 + (y_ - y0)**2 <= radius**2)
    # x, y = np.where((np.hypot((x_-x0)[:,np.newaxis], y_-y0)<= radius)) # alternative implementation
    for x, y in zip(x_[x], y_[y]):
        yield x, y
def moveRobot():
    pass
    
    
    
##funcion de para ealuar posisicon , busca las coordenadas del circuo , calcula la distancia y selecciona la mejor opcion
def evaluatePosition(radius,x,y,distance):
    candidates = points_in_circle_np(1,x,y)
    candidates= list(candidates)
    a = list(points_in_circle_np(2,0,0))
        ##separar las coordenadas en x y y
    aux=[]
    for i in candidates:
        for j in i :
                aux.append(j)
    print(aux)
    xcoordenates=[]
    ycoordenates=[]
    for idx,val in enumerate(aux):
        if idx%2 == 0:
                xcoordenates.append(val)
        else:
                ycoordenates.append(val)
        #obtiene la distancia de la clase main
    distance = main.distance
    coordenatelen = len(xcoordenates)
    for i in range(0,2):
            rand = randint(0,coordenatelen)
            
            

    



    




def getDistance(xo,yo,xf,yf):
    return math.sqrt(((xf-xo)*(xf-xo))+((yf-yo)*(yf-yo)))



