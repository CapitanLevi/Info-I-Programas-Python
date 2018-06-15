# L = [0, 4, 9]
# def modlist(L):
#     L[0]=5
#     return L


# # from string import ascii_letters
# # print(ascii_letters, range(28))
# # 
# # print(map(chr, range(97,123)))
# 
# L[1] = True
# print(L)
# 
# 
#  
# def myfunction(V):
#     V[1] = 0
#  
# m = input('m: ')
# print(myfunction(int(m)))
#  
#  
# def a():
#     s = 8
#     print(s)
# def b():
#     global s
#     s = 3
#     print(s)
# def c():
#     a = s + 1
#     print(a)

# import sys
# 
# com = None
# while com != 'q':
#     com = input('ing comando: ')
#     if com == 'exit':
#         print('Bye.')
#         raise SystemExit(0)
#         print('Didn\'t work')
# 
from termcolor import colored

print(colored('Hello, World!', color='magenta', attrs=['bold']))

# print(colored('Texto en amarillo con fondo azul', 'yellow', 'on_blue')+'hola')
# print(colored('Azul', color='blue'))
# 
# from colorama import *
# unit()
# from colorama import Fore, Back, Style
# print(Fore.RED + 'some red text')
# print(Back.GREEN + 'and with a green background')
# print(Style.DIM + 'and in dim text')
# print(Style.RESET_ALL)
# print('back to normal now')

# while True:
#     x = int(input())
#     y = int(input())
#     try:
#         result = x / y
#     except ZeroDivisionError:
#         print("¡división por cero!")
#         break
#     except TypeError:
#         a = 'Error de tipo ocurrido.'
#     else:
#         print("el resultado es", result)
#         continue
#     finally:
#         print("ejecutando la clausula finally")