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
# my_list_for_count = [int(i) for i in my_str if i.isdigit]

import random
import math

# def diff_max_min(def_list):
#     min_el, max_el = def_list[0]
#     for i in range(1,len(def_list)):
#         if min_el

# *Пример:*
# - для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21] 
my_num = int(input('Input number: '))

num_list = []
if my_num > 1: 
    for i in range(my_num+1):    
        num_list.append(random.randint(-my_num,my_num))
print(num_list)

with open("file1.txt", "r") as file1:
    list_pos_digs = file1.readlines()
    
mult_list = 1    
for pos in list_pos_digs:    
    if int(pos) < my_num:
        mult_list *= num_list[int(pos)]
        
print(f'Product digits from file.txt: {mult_list}')

    
