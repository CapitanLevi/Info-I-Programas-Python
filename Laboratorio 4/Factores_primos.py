print('Factores primos.')
n = 'a' # La asignación sólo sirve para ingresar al while

while n.lower() != 'q':
    try:
        n = int(input('Enter a number or Q to exit: '))
    except ValueError:
        continue

    while n%2 == 0:
        print(2)
        n = n//2
    else:
        for i in range(3, n+1, 2): # Función range(comienzo, número antes del final, paso)
            while n%i == 0:
                print(i)
                n = n//i
    n = str(n)