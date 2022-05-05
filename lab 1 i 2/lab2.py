import sys
import math

# zad1
# sporty = ['piłka nożna', 'siatkówka', 'skoki narciarskie']
# print(sporty)
# sporty.reverse()
# sporty.append('koszykówka')
# print(sporty)
# # zas2, 3
# skroty = {'np': 'na przykład', 'pt': 'pod tytułem'}
# print(skroty)
# print(len(skroty))
#
# #zad4
# zdanie = input('wpisz komunikat: ')
# print(zdanie.count('a'))
#
# # zad5
# sys.stdout.write('podaj a: ')
# a = sys.stdin.readline()
# sys.stdout.write('podaj b: ')
# b = sys.stdin.readline()
# sys.stdout.write('podaj c: ')
# c = sys.stdin.readline()
# a = int(a)
# b = int(b)
# c = int(c)
# sys.stdout.write(str(math.pow(a, b) + c))
#
# # zad6
# a = input("Wprowadź liczbę a: ")
# b = input("Wprowadź liczbę b: ")
# c = input("Wprowadź liczbę c: ")
#
# a = int(a)
# b = int(b)
# c = int(c)
# if a == b == c:
#     print("wprowadziłeś trzy takie same liczby")
# elif a >= b:
#     if a > c:
#         print("liczba",a,"jest największa")
#     else:
#         print("liczba",c, "jest największa")
# elif b > a:
#     if b > c:
#         print("liczba",b,"jest największa")
#     else:
#         print("liczba",c, "jest największa")
#
# # zad7
# lista = [5, 4, 2.6, 8, 4.1, 3]
# for a in lista:
#     print(a**2)
#
# # zad8
# licznik = 0
# liczby_pazyste = []
# while licznik < 10:
#     try:
#         liczba = input('wprowadź liczbę: ')
#         if float(liczba):
#             liczba = float(liczba)
#             if liczba % 2 == 0:
#                 liczby_pazyste.append(liczba)
#                 licznik += 1
#     except ValueError:
#         print('nie wczytano liczby')
# print(liczby_pazyste)
# print(len(liczby_pazyste))

# zad9
a = input('podaj liczbę: ')
try:
    a = int(a)
    pierwiastek = math.sqrt(a)
    print(pierwiastek)
except ValueError:
    if type(a) != int:
        print('nie wczytano liczby')
    elif a < 0:
        print('liczba a nie może być mniejsza od 0')