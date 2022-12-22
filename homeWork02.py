#  1   Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.

#     Пример:
# - 6782 -> 23
# - 0,56 -> 11

# почему-то такое решение приводит к ошибке в 
# def sum_numbers(num):
#     sum = 0    
#     while num % 10 > 0:
#         part = num % 10
#         num = int(num/10)
#         sum += part
#     return sum

# def float2int(num):
#     while (num * 10 - int(num * 10)) > 0:
#         num *= 10
#     return num  

# my_fl = float(input('Input number: '))
# print(sum_numbers(float2int(my_fl)))

my_str = input('Input number: ')
my_list_for_count = [int(i) for i in my_str if i in '123456789']
print(f'{my_str} -> {sum(my_list_for_count)}')

# 2 Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.

# *Пример:*
# - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

my_num = int(input('Input number: '))
multiple_list = [ 1 ]
if my_num > 1: 
    for i in range(1,my_num):    
        multiple_list.append(multiple_list[i-1] * (i+1))
print(multiple_list)

# 3 Задайте список из n чисел последовательности $(1+\frac 1 n)^n$ и выведите на экран их сумму.

# *Пример:*
# - Для n = 6: {1: 4, 2: 7, 3: 10, 4: 13, 5: 16, 6: 19}

my_num = int(input('Input number: '))
my_list = {i: 3*i+1 for i in range(1, my_num+1)}
print (f'Для n = {my_num}: {my_list}')

# 4 Задайте список из N элементов, заполненных числами из промежутка [-N, N]. 
# Найдите произведение элементов на указанных позициях. Позиции хранятся в файле file.txt в одной строке одно число.

my_num = int(input('Input number: '))

pos_list = []
if my_num > 1: 
    for i in range(-my_num,my_num+1,1):    
        pos_list.append(i)
print(pos_list)

with open("file.txt", "r") as file:
    digs = file.read()
        
digs_list = [int(i) for i in digs]
print(digs_list)

mult_from_file = 1
for i in range(len(pos_list)):
    mult_from_file *= digs_list[pos_list[i]]

print(f'Product digits from file.txt: {mult_from_file}')

# 5 Реализуйте алгоритм перемешивания списка.

import random

def rndmz_list(def_list):
    rnd_pos_list = []
    while len(rnd_pos_list) != len(def_list):
        new_rnd = random.randint(0,len(def_list)-1)
        if new_rnd not in rnd_pos_list:
            rnd_pos_list.append(new_rnd)
    print(rnd_pos_list)        
    
    new_def_list = []
    for i in range(len(def_list)):
        new_def_list.append(def_list[rnd_pos_list[i]])    
    return new_def_list        

lenght_list = 5
my_list = [random.randint(10,100) for i in range(lenght_list)]
print(my_list)
print(rndmz_list(my_list))

