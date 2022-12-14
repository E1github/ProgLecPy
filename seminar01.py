# Задачи:

# 1. Напишите программу, которая принимает на вход два числа и проверяет, является ли одно число квадратом другого.
    
#     *Примеры:* 
    
#     - 5, 25 -> да
#     - 4, 16 -> да
#     - 25, 5 -> да
#     - 8,9 -> нет
# 2. Напишите программу, которая на вход принимает 5 чисел и находит максимальное из них.
    
#     Примеры:
    
#     - 1, 4, 8, 7, 5 -> 8
#     - 78, 55, 36, 90, 2 -> 90

# x = int(input('Введите X: '))
# y = int(input('Введите Y: '))
# print(f'{x}, {y} -> ', end = '')

# # x, y = int (input())

# if x == y ** 2 or x ** 2 == y: 
#     print('да')
# else:
#     print('нет')

# list = list(input('Input:'))




numbers = []
for i in range(1,6):
    numbers.append(int(input(f'Введите элемент под номером {i}: ')))
print(numbers)
print(f'Максимальное {max(numbers)}')

my_max = 0
for _ in range(5):
    num = int(input('Введите число: '))
    if my_max < num:
        my_max = num

print(my_max)

