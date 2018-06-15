print('Cajero.')

valor = 'a'
Suma = 0
while valor.title() != 'Total':
    valor = input('Ingrese precio o "Total" para terminar: ')
    try:
        Suma += int(valor)
    except ValueError:
        continue
else:
    Impuesto = Suma * 0.16
    Total = Suma + Impuesto
    if 20000 <= Suma <= 50000:
        Desc = Total * 0.05
        Total -= Desc
        Ban = 20000
    elif Suma > 50000:
        Desc = Total * 0.08
        Total -= Desc
        Ban = 50000
        
print('\nTotal sin impuestos:',Suma)
print('Impuesto del 16%:',Impuesto)
try:
    if Ban == 20000 or Ban == 50000:
        print('Descuento del', ('5%' if Ban == 20000 else '8%'), 'por compras superiores a',str(Ban)+':', Desc)
        print('Total impuesto y descuento incluidos:',Total)
except NameError:
    print('Total impuesto incluido:',Total)
    