print('Liquidación de nómina.\n')

DS = int(input('Número trabajadores diurno semana: '))
DD = int(input('Número trabajadores diurno domingo: '))
NS = int(input('Número trabajadores nocturno semana: '))
ND = int(input('Número trabajadores nocturno dommingo: '))

PDS = DS*8*6*5*4
PDD = ND*(6*8+200)*4
PNS = NS*8*10*5*4
PND = ND*(10*8+300)*4

print('\nTotal a liquidar:', PDD + PDS + PND + PNS,'euros.')