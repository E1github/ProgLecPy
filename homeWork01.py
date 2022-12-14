# **Задачи:**

# 1. Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.
    
#     *Пример:*
    
#     - 6 -> да
#     - 7 -> да
#     - 1 -> нет
    
num = int(input('Enter number day of week: '))
if num in (6,7):
    print("yes")
elif num in (1,2,3,4,5):
    print("no")
else:
    print("incorrect number")
    
    
# 2. Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.

def input_nums(n):
    xyz = ["x", "y", "z"]
    a = []
    for i in range(n):
        a.append(input(f"Input number ({xyz[i]}): "))
    return a

def check_predicate(s):
    left = not (s[0] or s[1] or s[2])
    right = not s[0] and not s[1] and not s[2]
    result = left == right
    return result

print(f"It's {check_predicate(input_nums(3))}!")

# 3. Напишите программу, которая принимает на вход координаты точки (X и Y), причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, в которой находится эта точка (или на какой оси она находится).
   
#     *Пример:*
    
#     - x=34; y=-30 -> 4
#     - x=2; y=4-> 1
#     - x=-34; y=-30 -> 3

def input_nums(n):
    xy = ["x", "y"]
    a = []
    for i in range(n):
        a.append(int(input(f"Input coordinate ({xy[i]}): ")))
    return a

def area_num(xy):
    area = 4
    if xy[0] > 0 and xy[1] > 0:
        area = 1
    elif xy[0] < 0 and xy[1] > 0:
        area = 2
    elif xy[0] < 0 and xy[1] < 0:
        area = 3
    return area

print(f"This's coordinates belong to {area_num(input_nums(2))} area.")

# 4. Напишите программу, которая по заданному номеру четверти, показывает диапазон возможных координат точек в этой четверти (x и y).


num = int(input('Enter number of area: '))
if num == 1:
    print("X > 0, Y > 0")
elif num == 2:
    print("X < 0, Y > 0")
elif num == 3:
    print("X < 0, Y < 0")
elif num == 4:
    print("X > 0, Y < 0")
else:
    print("Incorrect number of area!")



# 5. Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.
    
#     *Пример:*
    
#     - A (3,6); B (2,1) -> 5,09
#     - A (7,-5); B (1,-1) -> 7,21

def input_nums(n):
    xy = ["x", "y"]
    a = []
    for i in range(n):
        a.append(int(input(f"Input coordinate ({xy[i]}): ")))
    return a

def lenghts2points(a,b):
    len = ((b[0] - a[0]) ** 2 + (b[1] - a[1]) ** 2) ** (0.5)
    return len

print(f"Lenghts = {lenghts2points(input_nums(2),input_nums(2))}")