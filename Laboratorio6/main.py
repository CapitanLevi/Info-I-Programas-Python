# Faltan los opcionales

from sudoku import *
printIntro("sudoku")
L = getRandomSudoku(5)
from copy import deepcopy
Copy = deepcopy(L)
printSudoku(L, Copy)
Historial=[]
cleard = {}

while True:
	# Entrada = 'e4 7', 'clear b7', 'clear board', 'new' o 'exit'
	if Completado(L) == False:
		pass
	elif Completado(L) == True:
		print('Felicidades, completó el sudoku.')
		#Usuario = input('Ingrese su nombre: ')
		#SaveGame(Usuario)
		break
	Entrada = input('Sudoku >>> ').lower()
	if Entrada == 'exit':
		break
	elif Entrada == 'new':
		L = getRandomSudoku(5) # Se carga otro sudoku
		Copy = deepcopy(L) # Se crea otra copia del mismo
		printSudoku(L, Copy) # Se imprime el nuevo sudoku
		continue
	elif Entrada == 'clear board':
		L = deepcopy(Copy) # Como la copia Copy siempre permanece intacta, basta con copiarla otra vez para L
		printSudoku(L, Copy)	# y volver a trabajar con L.
		continue
	elif Entrada[:6] == 'clear ' and len(Entrada) == 8: # Para 'clear h7' por ejemplo.
		if Clear(Entrada, L, Copy, cleard) == False:
			print('Entrada inválida.')
		else:
			L, cleard = Clear(Entrada, L, Copy, cleard) # En este caso el retorno de la función es la lista modificada.
			printSudoku(L, Copy)
			Historial.append(Entrada)
		continue
	elif Entrada == 'undo':
		L, Historial = Undo(Historial, L, Copy, cleard)
		printSudoku(L, Copy)
		continue
	elif validCoord(Entrada, Copy) == False: # De aquí en adelante, Entrada sólo será tipo 'd3 5'
		print('Entrada inválida')
		continue
	sen = True
	if checkFil(Letras.index(Entrada[0]), Entrada[3], L) == False:
		print('El número', Entrada[3] ,'ya existe en esa fila.')
		sen = False
	if checkCol(int(Entrada[1])-1, Entrada[3], L) == False:
		print('El número', Entrada[3] ,'ya existe en esa columna.')
		sen = False
	if checkBloque(Letras.index(Entrada[0]), int(Entrada[1])-1, Entrada[3], L) == False:
		print('El número', Entrada[3] ,'ya existe en ese bloque.')
		sen = False
	if sen == False: continue
	if validCoord(Entrada, Copy) == True:
		L[Letras.index(Entrada[0])][int(Entrada[1])-1] = Entrada[3]
		printSudoku(L, Copy)
		Historial.append(Entrada)
		