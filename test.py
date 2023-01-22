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

# users = ['user1', 'user2', 'user3', 'user4', 'user5']
# ids = [4, 5, 9, 114, 7]
# salary = [111, 222, 333]

# data = list(zip(users, ids, salary))
# print(data)


def print_gf(data_local):
    print(' ----------------- ')
    print(f'|  {data_local[1]}  |  {data_local[2]}  |  {data_local[3]}  |')
    print(' ----------------- ')
    print(f'|  {data_local[4]}  |  {data_local[5]}  |  {data_local[6]}  |')
    print(' ----------------- ')
    print(f'|  {data_local[7]}  |  {data_local[8]}  |  {data_local[9]}  |')
    print(' ----------------- ')

def user_turn(mark, data_local):
    print(f'Ход за {mark} ', end=': ')
    data_user = str(input())
    while data_user not in dict.values(data_local):
        print(f'Это поле уже занято, введите другой номер ', end=': ')
        data_user = input()
    data_local[int(data_user)] = mark

def check_end_game(positions):
    for i in 1, 2, 3:
        if positions[i] == positions[i + 3] == positions[i + 6]:
            return positions[i]
    for i in 1, 4, 7:
        if positions[i] == positions[i + 1] == positions[i + 2]:
            return positions[i]
    if positions[1] == positions[2] == positions[9]:
        return positions[1]
    if positions[3] == positions[5] == positions[7]:
        return positions[3]
    return False

flag = 'X'
data = {1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7', 8: '8', 9: '9'}
end_game = False
print_gf(data)

for turns in range(9):
    user_turn(flag, data)
    print_gf(data)
    end_game = check_end_game(data)
    if not end_game:
        flag = '0' if flag == 'X' else 'X'
    else:
        print(f'Победил {flag}! ')
else:
    print('Победила дружба!')
    
