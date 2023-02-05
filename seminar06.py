# 1. Напишите программу вычисления арифметического выражения заданного строкой. Используйте операции +,-,/,*. приоритет операций стандартный. 
#         *Пример:* 
#         2+2 => 4; 
#         1+2*3 => 7; 
#         1-2*3 => -5;
#         - Добавьте возможность использования скобок, меняющих приоритет операций.  
#         *Пример:* 
#         1+2*3 => 7;         
#         (1+2)*3 => 9;

user_input = input('Выражение ')

num_str = ''
parse = []
for sym in user_input:
   if sym.isdigit():
       num_str = num_str + sym
   else:
       parse.append(int(num_str))
       parse.append(sym)
       num_str = ''
parse.append(int(num_str))
print(parse)

while '*' in parse or '/' in parse:
    for i in range(1, len(parse) - 1, 2):
        if parse[i] == '*':
            oper2 = parse.pop(i + 1)
            oper1 = parse.pop(i - 1)
            parse[i-1] = oper1 * oper2
            break
        elif parse[i] == '/':
            oper2 = parse.pop(i + 1)
            oper1 = parse.pop(i - 1)            
            parse[i-1] = oper1 / oper2
            break
while '+' in parse or '-' in parse:
    for i in range(1, len(parse) - 1, 2):
        if parse[i] == '+':
            oper2 = parse.pop(i + 1)
            oper1 = parse.pop(i - 1)
            parse[i-1] = oper1 + oper2
            break
        elif parse[i] == '-':
            oper2 = parse.pop(i + 1)
            oper1 = parse.pop(i - 1)            
            parse[i-1] = oper1 - oper2
            break
    
print(parse)


        

        
# 43. Дана последовательность чисел. Получить список уникальных элементов заданной последовательности.
# *Пример:* 
# [1, 2, 3, 5, 1, 5, 3, 10] => [2, 10]
