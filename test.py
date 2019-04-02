import numpy as np 
from random import randint

def points_in_circle_np(radius, x0=0, y0=0, ):
    x_ = np.arange(x0 - radius - 1, x0 + radius + 1, dtype=int)
    y_ = np.arange(y0 - radius - 1, y0 + radius + 1, dtype=int)
    x, y = np.where((x_[:,np.newaxis] - x0)**2 + (y_ - y0)**2 <= radius**2)
    # x, y = np.where((np.hypot((x_-x0)[:,np.newaxis], y_-y0)<= radius)) # alternative implementation
    for x, y in zip(x_[x], y_[y]):
        yield x, y

a = list(points_in_circle_np(2,0,0))
##separar las coordenadas en x y y
aux=[]
for i in a:
        for j in i :
                aux.append(j)

xcoordenates=[]
ycoordenates=[]
for idx,val in enumerate(aux):
        if idx%2 == 0:
                xcoordenates.append(val)
        else:
                ycoordenates.append(val)
#obtiene la longitud de las coordenadas 
coordenatelen = len(ycoordenates)
print(coordenatelen)
#lista para guardar las coordenadas dentro de un rango positivo
coorinx =[]
cooriny=[]
for i in range(0,coordenatelen):
        if (xcoordenates[i]>=0) and (ycoordenates[i]>=0):
                coorinx.append(xcoordenates[i])
                cooriny.append(ycoordenates[i])
print(coorinx,cooriny)
#selecciona las coordenadas de la lista de manera aleatoria aleatorias 
for i in (0,2):
        rand =randint(0,2)
        print(rand)
        print(coorinx[rand],cooriny[rand])
        