print('Contraseña.')
Contraseña = '123'

for i in range(3):
    Contra = input('Ingrese contraseña: ')
    if Contra == Contraseña:
        print('Bienvenido al Curso de Informática I.')
        break
else:
    print('Lo sentimos, no acertaste.')