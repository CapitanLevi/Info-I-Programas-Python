n = input('ingrese nombre: ')
m = input('ingrese edad: ')
print('¡Hola', n+'!')

if n[len(n)-1].lower() == 'a': 
    print('Eres una mujer y tienes',m,'años')
else:
    print('Eres un hombre y tienes',m,'años')

ans = input('¿cierto? ')

if ans.lower() == 'sí':
    print('Já. Te caché.')
elif ans.lower() == 'no':
    print('ups, hablamos luego')