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

# import random

# list_originals = []
# list_work = [1, 1, 0 , 2, 3, 4, 4, 5, 6 ]
# for i in range(15):
#     list_work.append(random.randint(0,7))

# #не совсем конкретное задание ...
# for i in list_work:
#     if i not in list_originals:
#         list_originals.append(i)
# print(list_work)
# #если нужно вывести только неповторяющиеся значения, т.е. без дубликатов        
# print(list_originals)

# #если нужно вывести только неповторяющиеся значения, т.е. исключить то, что повторялись
# for i in list_originals:
#     if list_work.count(list_originals[i]) > 1:
#         while list_work.count(list_originals[i]) > 0:
#             list_work.pop(list_work.index(list_originals[i]))
# print(list_work)        

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