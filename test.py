# если есть возможность скорректировать план - есть предложение разбор ДЗ перенести на конец занятия, если это
# import math
# stepico

# x1, y1 = list(map(int, input('input coords(x1 y1) for first point separated by space - ').split()))
# x2, y2 = list(map(int, input('input coords(x2 y2) for first points separated by space - ').split()))

# print(round(math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2), 3))

# что можно было бы вписать в else что бы не добавляся элемент в новый лист если значение элемента 0?
# my_1st_list = [round(my_list[i]-int(my_list[i]),2) if round(my_list[i]-int(my_list[i]),2) > 0 else None for i in range(lenght_list)]

# почему isdigit не работает с точкой? признает ее за число и соответсвенно передает в данном коде?
# по тому, что нету скобок! чем отличается вызов со скоблками от вызова без скобок?
# my_str = input('Input number: ')
# my_list_for_count = [int(i) for i in my_str if i.isdigit()]
# # my_list_for_count = [int(i) for i in my_str if i in '123456789']
# print(f'{my_str} -> {sum(my_list_for_count)}')

# list_originals = []
# list_work = [1, 1, 0 , 2, 3, 4, 4, 5, 6 ]
# for i in list_work:
#     if i not in list_originals:
#         list_originals.append(i)        
# print(list_originals)
 # for j1 in range(len(expr1)):
    #     if i == int(expr1[j1][1]):
    #         k1 = int(expr1[j1][0])
    # for j2 in range(len(expr2)):
    #     if i == int(expr2[j2][1]):
            # k2 = int(expr2[j2][0])
# if int(expr_def_el[len(expr_def_el)-1]) > 0:
    #     expr_el_matrix.append(expr_def_el[len(expr_def_el)-1])
    
import random
import math
import re

# 5 Даны два файла, в каждом из которых находится запись многочлена. Задача - сформировать файл, содержащий сумму многочленов.
    
def file2list(filename):
    with open(filename, "r") as file_def:
        expr_def = file_def.readlines()
    print(expr_def)    
    expr_def[0] = expr_def[0].replace('+ ', '') #приводим строку удобному виду для распарсинга
    expr_def[0] = expr_def[0].replace('- ', '-')
    expr_def_el = re.split(r"\s=\s|\s", expr_def[0])
    expr_el_matrix = []    
    for i in range(len(expr_def_el)-1): #парсим и сохраняем, последнее значение после причесывания всегда 0 - откидываем 
        expr_el_matrix.append(re.split(r"\*x\^", expr_def_el[i]))    
    return expr_el_matrix
    
expr1 = file2list("hw4e5_1.txt")   
expr2 = file2list("hw4e5_2.txt")        
max_k = int(expr1[0][1]) if int(expr1[0][1]) > int(expr2[0][1]) else int(expr2[0][1])

flag = False #сложение и вывод, флаг для определения первого элемента
sum_expr = expr1 + expr2
for i in range(max_k,-1,-1):
    k = 0
    for j in range(len(sum_expr)):
        if i == int(sum_expr[j][1]):
            k += int(sum_expr[j][0])      
    if k != 0:
        plus = ' - ' if k < 0 else ' + ' if flag else ''
        print(f'{plus}{abs(k)}*x^{i}', end = '')
        flag = True
print(' = 0')                
        

