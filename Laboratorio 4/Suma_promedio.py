print('Suma y promedio.\n')
n = 1
suma = 0
numbers = -1
while n != 0:
    n = int(input('Enter a number: '))
    suma += n
    numbers += 1
promedio = suma / numbers
print('Suma:',suma)
print('Promedio:',promedio)