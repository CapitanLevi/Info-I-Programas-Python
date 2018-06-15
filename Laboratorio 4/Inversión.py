Inv = int(input('Ing cantidad a invertir: '))
Per = float(input('Ing interés mensual: '))

for i in range(12):
    Int = Inv*Per
    Inv = Inv + Int
    print('Para el mes', i+1,'llevas:', Inv)
    
print('Cantidad final:', Inv)