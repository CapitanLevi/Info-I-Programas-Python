from random import randint
n = randint(0,100)
intentos = 0
while True:
    entrada = input('Adivine un número entre 0 y 100: ')
    if n > float(entrada):
        print('Estás por debajo, inténtalo de nuevo.')
        intentos+=1
    if n < float(entrada):
        print('Estás por encima del número, una vez más.')
        intentos+=1
    if n == float(entrada):
        print('Acertáste!')
        intentos+=1
        print('Te tomó',intentos,'intentos lograrlo ¡Bien hecho!')
        break
    