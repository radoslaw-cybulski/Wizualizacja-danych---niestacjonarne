import random
from math import *

import ciagi.arytmetyczny
from ciagi import *

# lab3
# zad1
# a = [1-x for x in range(1, 11)]
# b = [4**x for x in range(0, 8)]
# c = [x for x in b if x % 2 == 0]
# print(a)
# print(b)
# print(c)
# zad2
# lista1 = []
# licznik = 0
# while licznik != 10:
#     a = random.randint(0, 100)
#     lista1.append(a)
#     licznik += 1
# print(lista1)
# nowa_lista = [x for x in lista1 if x % 2 == 0]
# print(nowa_lista)
# zad3
# slownik = {'mleko': 'sztuki', 'ziemiaki': 'kg', 'jogurt': 'sztuki'}
# lista = [key for key in slownik.keys() if slownik[key] == 'sztuki']
# print(lista)
# zad4
# def trojkat_prostokatny(a, b, c):
#     if a**2 + b**2 == c**2:
#         return 'trójtkąt prostokątny'
#     else:
#         return 'trójkąt nie jest prostokątny'
# print(trojkat_prostokatny(3, 4, 5))
# zad5
# def pole_trapezu(a=6,b=3,h=5):
#     return (a+b)*h/2
# print(pole_trapezu())
# # zad6
# def iloczyn(a=1, b=4, ile=10):
#     licznik = 0
#     while licznik != ile:
#         a *= b
#         licznik += 1
#     return a
# print(iloczyn())
# #zad7
# def iloczyn2(*liczby, b):
#     if len(liczby) == 0:
#         return 0
#     else:
#         iloczyn_liczb = liczby[0] * b
#         for a in range(1, len(liczby), 1):
#             iloczyn_liczb *= b
#         return iloczyn_liczb
# print(iloczyn2(1,2,3,4,5,6,7,8,9,10,b=4))
# zad8
# def lista_zakupow(** rzeczy):
#     koszt_zakupow = 0
#     for koszt in rzeczy:
#         koszt_zakupow += rzeczy[koszt]
#     return len(rzeczy), round(koszt_zakupow,2)
# print(lista_zakupow(mleko=2.78, czekolada=5.40, kawa=22.99))
# zad9
print(arytmetyczny.n_ty_wyraz(6, 6, 2))
print(arytmetyczny.suma_ciagu(6, 16, 6))
print(geometryczny.n_ty_wyraz(1, 4, 11))