#1     Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, 
# стоящих на нечётной позиции.

#     Пример:
# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12
import random

# def fill_list_int(num):
#     int_list = []
#     for i in range(num):
#         int_list.append(random.randint(1,10))
#     return int_list
   
def sum_odd_elem_inlist(def_list):
    sum = 0    
    for i in range(len(def_list)):
        if i % 2 != 0:            
            sum += def_list[i]
    return sum

lenght_list = 10
# my_list = fill_list_int(lenght_list)    
my_list = [random.randint(0,10) for i in range(lenght_list)]
my_odd_list = [my_list[i] for i in range(lenght_list) if i % 2 != 0] 
# my_list = [6, 10, 4, 10, 9]
print(f'{my_list} -> на нечётных позициях элементы {my_odd_list}, ответ: {sum_odd_elem_inlist(my_list)}')


# 2 Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.

# *Пример:*
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

import random

lenght_list = 6
my_list = [random.randint(1,10) for i in range(lenght_list)] 
# my_list = [2, 3, 4, 5, 6]
my_1st_list = [my_list[i] for i in range(0,lenght_list // 2)] 
my_2nd_list = [my_list[i] for i in range(-1,-(lenght_list // 2)-1, -1)] 
my_multi_list = [my_1st_list[i] * my_2nd_list[i] for i in range(lenght_list // 2)] 
if lenght_list % 2 != 0:
    my_multi_list.append(my_list[lenght_list % 2 + 1] ** 2)
print(f'{my_list} -> {my_multi_list}')

# 3 Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным 
# и минимальным значением дробной части элементов.

# *Пример:*
# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19
# правильный ответ 0.2 ??
import random
import math

lenght_list = 5
my_list = [round(random.randint(100,1000)/100,2) for i in range(lenght_list)]

# my_list = [1.1, 1.2, 3.1, 5, 10.01]
my_tail_list = [round(my_list[i]-int(my_list[i]),2) for i in range(lenght_list)] #для случая когда мы все же учитываем, что целое число имеет 0 на конце
# print(f'{my_list} -> {my_tail_list} -> {max(my_tail_list) - min(my_tail_list)}')

my_shorttail_list= []
for i in range(lenght_list):
    if my_tail_list[i]:
        my_shorttail_list.append(my_tail_list[i])
        
# что можно было бы вписать в else что бы не добавляся элемент в новый лист если значение элемента 0?
# my_1st_list = [round(my_list[i]-int(my_list[i]),2) if round(my_list[i]-int(my_list[i]),2) > 0 else None for i in range(lenght_list)]
# в таком случае задачу можно было бы решить в одну строку-)

# можно ли без round получить точный ответ при вычитании?   
print(f'{my_list} -> {my_shorttail_list} -> {max(my_shorttail_list) - min(my_shorttail_list)}')


# 4 Напишите программу, которая будет преобразовывать десятичное число в двоичное.

# *Пример:*
# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10

num10 = int(input('Input number: '))

delta_num10 = num10
num2str = ''
while delta_num10 > 0:
    num2str = str(delta_num10 % 2) + num2str
    delta_num10 = delta_num10 // 2
print(f'{num10} -> {num2str}')

# 5 Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.

# *Пример:*
# - для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21] 
# [Негафибоначчи](https://ru.wikipedia.org/wiki/%D0%9D%D0%B5%D0%B3%D0%B0%D1%84%D0%B8%D0%B1%D0%BE%D0%BD%D0%B0%D1%87%D1%87%D0%B8#:~:text=%D0%92%20%D0%BC%D0%B0%D1%82%D0%B5%D0%BC%D0%B0%D1%82%D0%B8%D0%BA%D0%B5%2C%20%D1%87%D0%B8%D1%81%D0%BB%D0%B0%20%D0%BD%D0%B5%D0%B3%D0%B0%D1%84%D0%B8%D0%B1%D0%BE%D0%BD%D0%B0%D1%87%D1%87%D0%B8%20%E2%80%94%20%D0%BE%D1%82%D1%80%D0%B8%D1%86%D0%B0%D1%82%D0%B5%D0%BB%D1%8C%D0%BD%D0%BE%20%D0%B8%D0%BD%D0%B4%D0%B5%D0%BA%D1%81%D0%B8%D1%80%D0%BE%D0%B2%D0%B0%D0%BD%D0%BD%D1%8B%D0%B5%20%D1%8D%D0%BB%D0%B5%D0%BC%D0%B5%D0%BD%D1%82%D1%8B%20%D0%BF%D0%BE%D1%81%D0%BB%D0%B5%D0%B4%D0%BE%D0%B2%D0%B0%D1%82%D0%B5%D0%BB%D1%8C%D0%BD%D0%BE%D1%81%D1%82%D0%B8%20%D1%87%D0%B8%D1%81%D0%B5%D0%BB%20%D0%A4%D0%B8%D0%B1%D0%BE%D0%BD%D0%B0%D1%87%D1%87%D0%B8.)

def fib(n):
    fib_list = [0]
    x, y = 0, 1
    for i in range(n):
        x, y = y, x + y
        fib_list.append(x)
        fib_list.insert(0, -x if i %2 else x)
    return fib_list

fib_num = int(input('Input number: '))
print(f'для k = {fib_num} список будет выглядеть так: {fib(fib_num)}')