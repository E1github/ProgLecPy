# def check(stringlist: list, n: str) -> bool:
#     for i in stringlist:
#         if n == i:
#             return True
#     return False

# my_list = ["2", "3", "3425", "0", "-1"]
# x = input("Введите искомое число: ")
# if check(my_list, x):
#     print("Число есть в последовательности", my_list)
# else:
#     print("Числа нет в последовательности", my_list)

# my_list = ["2", "3", "3425", "0", "-1"]
# x = input("Введите искомое число: ")

# print (x in my_list)

# 3. Напишите программу, которая определит позицию второго вхождения строки в списке либо сообщит, что её нет.

# *Пример:*

# - список: ["qwe", "asd", "zxc", "qwe", "ertqwe"], ищем: "qwe", ответ: 3
# - список: ["йцу", "фыв", "ячс", "цук", "йцукен", "йцу"], ищем: "йцу", ответ: 5
# - список: ["йцу", "фыв", "ячс", "цук", "йцукен"], ищем: "йцу", ответ: -1
# - список: ["123", "234", 123, "567"], ищем: "123", ответ: -1
# - список: [], ищем: "123", ответ: -1

# def check(stringlist: list, n: str):
#     for i in stringlist:
#         if n == i:
#             return True
#     return False
# my_list = ["qwe", "asd", "zxc", "qwe", "ertqwe"]
# x = input("Введите строку: ")
# print (my_list)

# my_list= ["йцу", "фыв", "ячс", "цук", "йцукен", "йцу"]
# print(my_list)
# string_find = "йцу"
# count = 0
# for i in range(len(my_list)):
#     if string_find == my_list[i]:
#         count+=1
#         if count == 2:
#             print(i)
#             break
# else:
#     print(-1)
    
# my_list= ["йцу", "фыв", "ячс", "цук", "йцукен", "йцу"]
# print(my_list)
# string_find = "йу"
# count = -1
# for i in range(len(my_list)):
#     if string_find == my_list[i]:
#         count+=1
#         if count == 1:
#             count = i
#             print(i)
#             break
# else:
#     print(count)


my_list= ["йцу", "фыв", "ячс", "цук", "йцукен", "йцу"]
my_str = input('Введите строку')

if my_list.count(my_str) > 1:
    first_index = my_list.index(my_str)
    print(my_list.index(my_str, first_index + 1))
else:
    print(-1)


