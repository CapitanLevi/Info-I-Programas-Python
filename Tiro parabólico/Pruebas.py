from numpy import linspace, tan, cos
from matplotlib import pyplot
# x = numpy.linspace(0, 2 * numpy.pi, 1000)
# y = numpy.sin(x)
# pyplot.plot(x, y)
# pyplot.show()
def sec(theta):
    return 1/cos(theta)
g=9.8
Vo=float(input('Ingrese verlocidad inicial: '))
theta=float(input('Ingrese ángulo: '))
x = linspace(0, 6.75, 1000)
y = x*tan(theta)-(x**2)*(g*(sec(theta))**2)/(2*Vo**2)
pyplot.plot(x, y)
pyplot.show()