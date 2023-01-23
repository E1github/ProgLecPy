##LAMBDA

# 5. Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.
    
#     *Пример:*
    
#     - A (3,6); B (2,1) -> 5,09
#     - A (7,-5); B (1,-1) -> 7,21

def input_nums(n):
    xy = ["x", "y"]
    a = []
    for i in range(n):
        a.append(int(input(f"Input coordinate ({xy[i]}): ")))
    return a

def lenghts2points(a,b):
    # было
    # len = ((b[0] - a[0]) ** 2 + (b[1] - a[1]) ** 2) ** (0.5)
    #реализуем лямбдой возведение в квадрат
    my_sqr = lambda x: x ** 2
    len = (my_sqr(b[0] - a[0]) + my_sqr(b[1] - a[1])) ** (0.5)
    return len

print(f"Lenghts = {lenghts2points(input_nums(2),input_nums(2))}")

###MAP

import math

#реализация ввода через мэп
x1, y1 = list(map(int, input('input coords(x1 y1) for first point separated by space - ').split()))
x2, y2 = list(map(int, input('input coords(x2 y2) for first points separated by space - ').split()))

print(round(math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2), 3))

###list comprehension

# 3 Задайте список из n чисел последовательности $(1+\frac 1 n)^n$ и выведите на экран их сумму.

# *Пример:*
# - Для n = 6: {1: 4, 2: 7, 3: 10, 4: 13, 5: 16, 6: 19}

#сразу было решено было через компрехеншион, можно переделать обычно и потом наоборот-)
my_num = int(input('Input number: '))
my_list = {i: 3*i+1 for i in range(1, my_num+1)}
print (f'Для n = {my_num}: {my_list}')

###ZIP
#пока вроде использования зип необходимости не возникало, по крайне мере не придумал
#возможно в задаче на импорт телефонного справочника пригодится - типа
contacts = ['contact1', 'contact2', 'contact3', 'contact4', 'contact5']
phones = [444444, 55555, 99999, 11111, 77777]
data = list(zip(contacts, phones))
print(data)
