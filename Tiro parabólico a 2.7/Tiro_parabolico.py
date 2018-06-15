#Programa que simula un lanzamiento de baloncesto desde la linea de 3 puntos.

from math import cos, tan, atan, sqrt, pi
import numpy as np
from matplotlib import pyplot
def sec(alpha):
    return 1/cos(alpha)

##Variables de entrada
#Altura inicial: altura del jugador mas 30 cm (promedio de levantamiento del brazo por encima de la cabeza)
Hjugador = float(raw_input('Ingrese su altura en metros (Ej: 1.65): '))
Yo = Hjugador + 0.3
#Altura final: altura del arco - altura inicial.
Hfinal = 3.05 - Yo
#Altura maxima
Hmax = float(raw_input('Que tan alto desea lanzar el balon respecto al suelo?: '))
#Distancia maxima horizontal. Se hace el lanzamiento desde la circunferencia de los 3 puntos.
Xmax = 6.75
#Aceleracion de la gravedad
g = 9.8

##Variables de salida: Tiempo de vuelo, velocidad inicial y angulo de lanzamiento.
Tv = sqrt(2/g)*(sqrt(Hmax)+sqrt(Hmax-Hfinal))
alpha = atan((2*Hfinal+g*(Tv**2))/13.5)
Vo = 6.75/(Tv*cos(alpha))

print('Tiempo de vuelo:',round(Tv,2),'segundos')
print('Altura desde la mano del jugador levantada hasta el aro:',round(Hfinal,2),'metros')
print('Velocidad inicial:',round(Vo,2),'m/s')
print('Angulo de lanzamiento:',round(alpha*180/pi,2),'grados')

#Grafica de la trayectoria del balon.
x=np.linspace(0, Xmax, 1000)
y = x*tan(alpha)-(x**2)*(g*(sec(alpha))**2)/(2*Vo**2)
pyplot.plot(x, y)
pyplot.show()

#---------------------Animacion----------------------#
import visual as vs
## valores iniciales (modificalos bajo tu responsabilidad)
v0 = Vo # En m/s. Importado desde main
alfa = alpha # Angulo en radianes. Importado desde main
## Constantes
g = 9.8 ## Aceleracion de la gravedad
## Ecuaciones
v0x = v0 * np.cos(alfa)
v0z = v0 * np.sin(alfa)
t_total = Tv
x_final = 6.75
## Empezamos con visual python (vpython)
## Creamos el 'suelo'
suelo = vs.box(pos = (x_final/2., -1, 0),
               size = (x_final, 1, 10), color = vs.color.green)
## Creamos el 'canon'
canyon = vs.cylinder(pos = (0, 0, 0),
                     axis = (2 * np.cos(alfa), 2 * np.sin(alfa), 0), size=(0,0,0,0))
## Creamos el proyectil y una linea que dejara la estela del proyectil
bola = vs.sphere(pos = (0, 0, 0), radius=0.5, color=vs.color.magenta)
bola.trail = vs.curve(color=vs.color.cyan)
## Creamos el vector que indica la direccion del movimiento (vector velocidad)
flecha = vs.arrow(pos = (0, 0, 0),
                  axis = (v0x, v0z, 0), color = vs.color.yellow, size=(0))
## texto (ponemos etiquetas para informar de la posicion del proyectil)
labelx = vs.label(pos = bola.pos, text= 'posicion x = 0 m', xoffset=1,
                  yoffset=80, space=bola.radius, font='sans', box = False,
                  height = 10)
labely = vs.label(pos = bola.pos, text= 'posicion y = 0 m', xoffset=1,
                  yoffset=40, space=bola.radius, font='sans', box = False,
                  height = 10)
## Animamos todo el cotarro!!!
t = 0
while t <= t_total:
    bola.pos = (v0x * t, v0z * t - 0.5 * g * t**2, 0)
    flecha.pos = (v0x * t, v0z * t - 0.5 * g * t**2, 0)
    flecha.axis = (v0x, v0z - g * t, 0)
    bola.trail.append(pos=bola.pos)
    labelx.pos = bola.pos
    labelx.text = 'posicion x = %s m' % str(v0x * t)
    labely.pos = bola.pos
    labely.text = 'posicion y = %s m' % str(v0z * t - 0.5 * g * t**2)
    t = t + t_total / 100.
    vs.rate(10) #Velocidad de los fotogramas
