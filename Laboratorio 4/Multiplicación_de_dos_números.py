print('Ingrese dos números a multiplicar.')
a, b = [int(k) for k in input().split()]
count = 0
suma = 0
while count < a:
    suma += b
    count += 1
print('Resultado: ', suma)

a, b = [int(k) for k in input().split()]
count = b
result = 0
while count > 0:
    result += a
    count -= 1
print('resultado: ', result)