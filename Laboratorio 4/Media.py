print('Número del medio entre tres.\n')
mayor = -99999999999999
menor = 99999999999999

for i in range(3):
    n = int(input('Ing número: '))
    if n > mayor and n < menor:
        medio = n
    elif n >= mayor and n > menor:
        mayor = n
    elif n < mayor and n <= menor:
        menor = n
    
    print(mayor)
    print(medio)
    print(menor)
    print()