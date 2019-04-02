import numpy as np
import math
from random import randint

distance = getDistance()

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
    candidates = points_in_circle_np(radius,x,y)
    candidateslen = len(candidates)
    




def getDistance(xo,yo,xf,yf):
    return math.sqrt(((xf-xo)*(xf-xo))+((yf-yo)*(yf-yo)))



