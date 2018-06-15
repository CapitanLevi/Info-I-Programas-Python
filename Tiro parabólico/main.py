#Programa que simula un lanzamiento de baloncesto desde la línea de 3 puntos.
from cmath import *
from math import *
from numpy import *
from matplotlib import pyplot
def sec(theta):
    return 1/cos(theta)

##Variables de entrada
#Altura inicial: altura del jugador más 30 cm (promedio de levantamiento del brazo por encima de la cabeza)
Hjugador = float(input('Ingrese su altura en metros (Ej: 1.65): '))
Yo = Hjugador + 0.3
#Altura final: altura del arco - altura inicial.
Hfinal = 3.05 - Yo
#Altura máxima
Hmax = float(input('¿Qué tan alto desea lanzar el balón respecto al suelo?: '))
#Distancia máxima horizontal. Se hace el lanzamiento desde la circunferencia de los 3 puntos.
Xmax = 6.75
#Aceleración de la gravedad
g = 9.8

##Variables de salida: Tiempo de vuelo, velocidad inicial y ángulo de lanzamiento.
Tv = sqrt(2/g)*(sqrt(Hmax)+sqrt(Hmax-Hfinal))
theta = atan((2*Hfinal+g*(Tv**2))/13.5)
Vo = 6.75/(Tv*cos(theta))

print('Tiempo de vuelo:',Tv,'segundos')
print('Velocidad inicial:',Vo)
print('Ángulo de lanzamiento:',theta)

#Gráfica de la trayectoria del balón.
x=linspace(0, Xmax, 1000)
y = x*tan(theta)-(x**2)*(g*(sec(theta))**2)/(2*Vo**2)
pyplot.plot(x, y)
pyplot.show()
