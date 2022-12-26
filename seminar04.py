# 1. Задайте строку из набора чисел. Напишите программу, которая покажет большее и меньшее число. В качестве символа-разделителя используйте пробел.
import random

def random_str(num_list):
    str1 = ''
    for i in range(10):
        str1 = str1 + str(num_list[i])+' '
    return str1

lenght_list = random.randint(0,20) 
   
my_list = [random.randint(0,10) for i in range(lenght_list)]
my_str = random_str(my_list)

print(my_list)
print(my_str)

my_list1 = my_str.split()

print(f' в списке {my_list1} максимальный элемент = {max(my_list1)} минимальный = {min(my_list1)}')



# 2. Найдите корни квадратного уравнения Ax² + Bx + C = 0 двумя способами:
    
#     1) с помощью математических формул нахождения корней квадратного уравнения
    
#     2) с помощью дополнительных библиотек Python

# a/c * x ** 2 + b/c * x = -1

# a = int(input('A : '))
# b = int(input('B : '))
# c = int(input('C : '))

list_num = input('Input a, b, c:').split()
a, b, c = list(map(int, list_num))

d = b ** 2 - 4 * a * c

if d < 0:
    print('Корней нет')
elif d == 0:
    x = -b / (2 * a)
    print(f'x_ = {x}', end=' ')
else:
    x1 = (-b + d ** 0.5) / (2 * a)
    print(f'x1_ = {x1}', end=' ')
    x2 = (-b - d ** 0.5) / (2 * a)
    print(f'x2_ = {x2}')


    
# 3. Задайте два числа. Напишите программу, которая найдёт НОК (наименьшее общее кратное) этих двух чисел.

# НОК(a, b)=a⋅b:(a, b)=a•b:НОД(a, b)
# Ответ:  НОК (99, 54) = 594
# 99*54=5346
# 594/99 = 6, 594/54=11

a, b = int(input('Введите a')), int(input('Введите b'))
max_num = max(a, b)
for i in range(max_num, (a * b) + 1, max_num):
    if i % a == i % b == 0:
        print(i)
        break

