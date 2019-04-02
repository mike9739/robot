import robot as robot
##pregunta por la dimension del escenario
mapwidth=input('introduzca el ancho del mapa:')
mapwidth= int(mapwidth)
mapheight=input('introduzca la altura del mapa:')
mapheight=int(mapheight)
mapa = robot.createWorld(mapheight,mapheight)
print(mapa)
##pregunta por donde va a empezar el robot
xinicial = input('Por favor introduzca la coordenada inicial en x:')
xinicial = int(xinicial)
yinicial = input('Por favor introduzca la coordenada inicial en y:')
yinicial = int(yinicial)
mapa[yinicial][xinicial]=1
print('El robot se ubica aqui:')
print(mapa)

#pregunta por las coordenadas  en donde va a estar el objetivo a llegar
xfinal = input('Por favor introduzca la coordenada final en x:')
xfinal = int(xfinal)
yfinal = input('Por favor introduzca la coordenada final en y:')
yfinal = int(yfinal)
mapa[yfinal][xfinal]=2
print('El objetivo se encuentra aqui:')
print(mapa)

distance = robot.getDistance(xinicial,yinicial,xfinal,yfinal)
print(distance)

