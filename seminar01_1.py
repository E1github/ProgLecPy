# **Задачи:**

# 1. Напишите программу, которая будет на вход принимать число N и выводить числа от -N до N
    
#     *Примеры:* 
    
#     - 5 -> -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5
# 2. Напишите программу, которая будет принимать на вход дробь и показывать первую цифру дробной части числа.
    
#     *Примеры:*
    
#     - 6,78 -> 7
#     - 5 -> нет
#     - 0,34 -> 3
# 3. Напишите программу, которая принимает на вход число и проверяет, кратно ли оно 5 и 10 или 15, но не 30.


# n = int(input('Введите N: '))
# if n < 0:
#     n = -n  
# print(f'{n} ->', end='')     
# for i in range(-n,n+1):
#     print(f'{i}, ', end='')

#2
# n = float(input('Введите N: '))
# a = int(n*10 % 10)
# print(a)
# n //=1
# print(n)



# num = float(input('Введите дробное число: '))
# if num % 1 == 0:
#     print('нет')
# else:
#     num = int(num*10 % 10)
#     print(num)



# num = input('Введите дробное число: ')
# if num.isdigit():
#     print('нет')
# else:
#     num = int(float(num)*10 % 10)
#     print(num)



# num = int(input('Enter number: '))
# if num % 30 == 0:
#     print("no")
# elif num % 5 == 0 and num % 10 == 0 or num % 15 == 0:
#     print('yes')
# else:
#     print('no')


user_number = float(input('Enter your number: '))

if (user_number % 5 == 0 and user_number % 10 == 0 or user_number % 15 == 0) and user_number % 30 != 0:
    print('Your number is nice! :)')
else:
    print('Try again.')
