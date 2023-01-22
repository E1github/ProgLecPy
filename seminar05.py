# 35. В файле находится N натуральных чисел, записанных через пробел. Среди чисел не хватает одного, 
# чтобы выполнялось условие A[i] - 1 = A[i-1]. Найдите это число.

# def file2list(filename):
#     with open(filename, "r") as file_def:
#         expr_def = file_def.readlines()
#     expr_l = expr_def[0].split()
#     return expr_l
        
# expr = file2list("sm5e1.txt")
# print(expr)

# for j in range(len(expr)-1):
#     if int(expr[j+1]) - int(expr[j]) > 1 :
#         print(int(expr[j])+1)
        
# for i, elem in enumerate(num_row[:-1]):
#     if elem + 1 != num_row[i+1]:
#         print(elem + 1)
#         break



# 1. Дан список чисел. Создайте список, в который попадают числа, описываемые возрастающую последовательность.
# Порядок элементов менять нельзя.
#     *Пример:* 
#     [1, 5, 2, 3, 4, 6, 1, 7] => [1, 2, 3] или [1, 7] или [1, 6, 7] и т.д.
    
num_list = [1, 5, 2, 3, 4, 6, 1, 7]  
print(num_list, end=' => ')

for n in range(4,len(num_list)):
    for i in range(len(num_list)):
        order_list = []
        order_list.append(num_list[i])
        min_num = num_list[i] 
        for j in range(i,len(num_list)):
            if num_list[j] > min_num:
                min_num = num_list[j]
                order_list.append(num_list[j])
            if len(order_list) == n:
                print(order_list, end=' ')
                break
       
my_list = [1, 2, 3, 5, 1, 5, 3, 10]
print(my_list)
my_set = list(set(my_list))
print(my_set)

# 38. Напишите программу, удаляющую из текста все слова, содержащие "абв".


# my_str = 'АБВ ылоажы фыыдлх абв Зщышф вабвв ффлжв абВ'
# new_str = ' '.join(list(filter(lambda elem: 'абв' not in elem.lower(), my_str.split())))
# print(new_str)
