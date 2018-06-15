x1, y1 = [int(k) for k in input('Enter P1 coords: ').split()]
x2, y2 = [int(k) for k in input('Enter P2 coords: ').split()]
x3, y3 = [int(k) for k in input('Enter P3 coords: ').split()]

a = (x1 - x2)**2 + (y1 - y2)**2
b = (x1 - x3)**2 + (y1 - y3)**2
c = (x3 - x2)**2 + (y3 - y2)**2

if a == b + c or b == a + c or c == a + b:
    print('Es rectágulo.')
else: print('No es rectángulo.')