from math import sqrt 

xA = float (input(''))
xB = float (input(''))
yA = float (input(''))
yB = float (input(''))

distanciaAB = sqrt((xA-xB) **2) + ((yA- yB) **2)

print('A distancia entre esses dois pontos é de:', distanciaAB, 'unidades de medida')