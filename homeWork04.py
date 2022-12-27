# Урок 4. Данные, функции и модули в Python. Продолжение

#1     Вычислить число c заданной точностью d

#     Пример:
# - при $d = 0.001, π = 3.141.$    $10^{-1} ≤ d ≤10^{-10}$

import math
#не совсем понятно какое число нужно вычислить, давайте вычислим длинну окружности ...
d = 0.001
num10 = int(input('Input precision in number of decimal places: ')) 
print(f'Length of circle wit D = {d} is {round(d * math.pi,num10)}')
#хотя, если нам нужно вычислить само число Пи..
print(round(99999999*math.sin(math.radians(180/99999999)), num10))
#или через лейбница, но через синус точнее, при одинаковой загрузке на ЦП
pi_calc, multiplier = 0, -1
for i in range(1,99000000,2):
    multiplier *= -1
    pi_calc += multiplier*4/i
print(round(pi_calc,num10))


# 2 Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.

def is_simple_number(num) -> bool: 
    is_simple = 1
    for i in range(2,num):        
        is_simple = is_simple * num % i                 
    return is_simple

num10 = int(input('Input number: '))
simple_mult_list = [int(i) for i in range(1,num10) if is_simple_number(i)] #список простых чисел со второго ибо 1 не надо
mult = [[simple_mult_list[i], "x "+str(num10 // simple_mult_list[i])] for i in range(len(simple_mult_list)) if num10 % simple_mult_list[i] == 0]
print(f'\n Simple multiplires for {num10} is: {mult}') # 1271 9999

 
# 3 Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.
import random

list_originals = []
list_work = [1, 1, 0 , 2, 3, 4, 4, 5, 6 ]
for i in range(15):
    list_work.append(random.randint(0,7))

#не совсем конкретное задание ...
for i in list_work:
    if i not in list_originals:
        list_originals.append(i)
print(list_work)
#если нужно вывести только неповторяющиеся значения, т.е. без дубликатов        
print(list_originals)

#если нужно вывести только неповторяющиеся значения, т.е. исключить те, что повторялись
for i in list_originals:
    if list_work.count(list_originals[i]) > 1:
        while list_work.count(list_originals[i]) > 0:
            list_work.pop(list_work.index(list_originals[i]))
print(list_work)        
        

# 4 Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена и записать 
# в файл многочлен степени k.

# *Пример:* 
# - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0
import random

sum = int(input('Input K: '))

print(f'k = {sum} -> ', end = '')
null_elems = 0
for i in range(sum,-1,-1):    
    num = random.randint(0,100)
    
    if num == 0: #проверка на необходимость знака '+' при пустых первых значениях
        null_elems += 1
        continue
    plus = ' + ' if sum - null_elems != i else ''
        
    if i == sum:
        print(f'{num}*x^{i}', end = '')
    elif i != 0: 
        print(f'{plus}{num}*x^{i}', end = '')
    elif i == 1: 
        print(f'{plus}{num}*x', end = '')
    else:
        print(f'{plus}{num}', end = '')
        
print(' = 0')

# 5 Даны два файла, в каждом из которых находится запись многочлена. Задача - сформировать файл, содержащий сумму многочленов.
import re

#раз не указано иного, полагаем что многочлены в файлах храняться в формализованном виде: A*x^B, а приравниваются 0
#                                                                                      где A от -n до n, a B от 0 до m 

def file2list(filename):
    with open(filename, "r") as file_def:
        expr_def = file_def.readlines()
    print(expr_def)    
    expr_def[0] = expr_def[0].replace('+ ', '') #приводим строку к удобному виду для распарсинга
    expr_def[0] = expr_def[0].replace('- ', '-')
    expr_def_el = re.split(r"\s=\s|\s", expr_def[0]) 
    expr_el_matrix = []    
    for i in range(len(expr_def_el)-1): #парсим и сохраняем. последнее значение после причесывания всегда 0 - откидываем 
        expr_el_matrix.append(re.split(r"\*x\^", expr_def_el[i]))
    #при необходимости можно усложить парсинг для случая ввода сведений при B = 0 и 1 в более "человеческом виде"    
    return expr_el_matrix
    
expr1 = file2list("hw4e5_1.txt")   
expr2 = file2list("hw4e5_2.txt")        
max_k = int(expr1[0][1]) if int(expr1[0][1]) > int(expr2[0][1]) else int(expr2[0][1])

flag = False #сложение и вывод, флаг определения первого элемента для корректного отображения
sum_expr = expr1 + expr2
result_expr = ''
for i in range(max_k,-1,-1):
    sum = 0
    for j in range(len(sum_expr)):
        if i == int(sum_expr[j][1]):
            sum += int(sum_expr[j][0])      
    if sum != 0:
        plus = ' - ' if sum < 0 else ' + ' if flag else ''
        result_expr += str(plus)+str(abs(sum))+'*x^'+str(i)
        # print(f'{plus}{abs(sum)}*x^{i}', end = '')
        flag = True
        
result_expr += ' = 0'        
print(result_expr) 
with open("hw4e5_res.txt", "w") as file:
    file.write(result_expr)