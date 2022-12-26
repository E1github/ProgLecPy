## Групповая работа [2]

# 1. Напишите программу, которая принимает на вход число N и выдаёт последовательность из N членов.
    
#     *Пример:*
    
#     - Для N = 5: 1, -3, 9, -27, 81
# import random

# num = int(input('Input number: '))

# for i in range(num):
#     print(random.randrange(-100, 100))
   
    
    
# 2. Для натурального n создать словарь индекс-значение, состоящий из элементов последовательности 3n + 1.
    
#     *Пример:*
num = int(input('Input number: '))
my_list = []
for i in range(1,num+1):
    my_list.append([i,3*i+1])
    
print(my_list)
# my_list.clear    
# print(my_list1)

# n = int(input('введите число '))
# slovar = {}
# for i in range(1, n+1):
#  slovar.update({i:3*i+1})
# print(slovar)

    
#     - Для n = 6: {1: 4, 2: 7, 3: 10, 4: 13, 5: 16, 6: 19}


# 3. Напишите программу, в которой пользователь будет задавать две строки, а программа - определять 
# количество вхождений одной строки в другой.

str1 = 'a b'
str2 = 'ab ab a b ba ff'

# str2.find(str1)

print(str2.count(str1))




n = int(input('Print your N: '))
my_dict = {} # словарь
# my_list =[]  список
for i in range(1,n+1):
    my_dict[i] = 3*i + 1
print(my_dict)



num = int(input("Ведите число: "))
d = {a: 3*a+1 for a in range(1, num+1)}
print (d)



first_string = 'овкукареку ку кук'
second_string = 'ку'
count = 0
for i in range(len(first_string) - len(second_string)):
    if first_string[i] == second_string[0]:
        flag = True
        for j in range(1, len(second_string)):
            if second_string[j] != first_string[i+j]:
                flag = False
        if flag:
            count += 1
print(count)
