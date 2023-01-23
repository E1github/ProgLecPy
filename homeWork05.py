# 1.    Напишите программу, удаляющую из текста все слова, содержащие ""абв"".
my_str = 'АБВ ылоажы фыыдлх абв Зщышф вабвв ффлжв абВ'
new_str = ' '.join(list(filter(lambda elem: 'абв' not in elem.lower(), my_str.split())))
print(new_str)
# 2.    Создайте программу для игры с конфетами человек против человека.
#     Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга. 
# Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет. 
# Все конфеты оппонента достаются сделавшему последний ход. Сколько конфет нужно взять первому
# игроку, чтобы забрать все конфеты у своего конкурента?
#     a) Добавьте игру против бота
#     b) Подумайте как наделить бота ""интеллектом""
import random

def player_round(max_num, num, player):
    take_candy = -1
    while 0 > take_candy or take_candy > max_num or take_candy > num:
        take_candy = int(input(f'Сколько конфет из {num} возмет игрок {player}? '))
        if take_candy > max_num:
            print(f'Не надо быть жадным - максимально количество конфет которые можно взять -  {max_num}!')
        elif take_candy > num:
            print(f'Осталось всего {num} кофет!')
        elif take_candy == 0:
            print(f'Надо взять минимум одну конфету!')
    return take_candy

def bot_round(max_num, num):
    if num <= max_num:
        take_candy = num
    elif num > max_num and num - max_num <= max_num + 1:
        take_candy = num - max_num - 1
    else:
        take_candy = num - (num // (max_num + 1)) * (max_num + 1) + 1
    take_candy = 1 if take_candy == 0 or take_candy > max_num else take_candy
    print(f'Бот берет {take_candy} конфет(у).')
    return take_candy    

candy = 2021
max_candy = 28
print(f'  На столе лежит {candy} конфет(а). Играют два игрока делая ход друг после друга. \
Первый ход определяется жеребьёвкой.\nЗа один ход можно забрать не более чем {max_candy} конфет. \
Все конфеты оппонента достаются сделавшему последний ход. Если хотите играть с ботом - введите имя "bot".')
p_name = []
p_name.append(input("Имя первого игрока: "))
p_name.append(input("Имя второго игрока: "))

in_game_player = random.randint(0,1)

print(f'Первым ходит игрок {p_name[in_game_player]}')
   
game_candy = candy

while game_candy > 0:
    if 'bot' not in p_name[in_game_player]:
        game_candy -= player_round(max_candy, game_candy, p_name[in_game_player])
    else:
        game_candy -= bot_round(max_candy, game_candy)
    print(f'Осталось конфет - {game_candy}.')
    in_game_player = int(not bool(in_game_player))
print(f'Победил игрок {p_name[int(not bool(in_game_player))]}!')

#3.     Создайте программу для игры в ""Крестики-нолики"".

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

def check_end_game(data_local):
    for i in 1, 2, 3:
        if data_local[i] == data_local[i + 3] == data_local[i + 6]:
            return data_local[i]
    for i in 1, 4, 7:
        if data_local[i] == data_local[i + 1] == data_local[i + 2]:
            return data_local[i]
    if data_local[1] == data_local[2] == data_local[9]:
        return data_local[1]
    if data_local[3] == data_local[5] == data_local[7]:
        return data_local[3]
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
        print(f'Победил {flag} ! ')
else:
    print('Победила дружба!')

# 4.    Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Входные и выходные данные хранятся в отдельных текстовых файлах.

def create_txt_file(filename):
    with open(filename, "w") as compressed_txt:
        print(f'Введите строку для сжатия :')
        input_txt = input()
        compressed_txt.writelines(rle_compress(input_txt))    
        
def rle_compress(txt):
    compressed_str = ''
    symb_count = 1
    for i in range(len(txt) - 1):
        if txt[i] == txt[i + 1]:
            symb_count +=1
        else:
            compressed_str += str(symb_count) + txt[i]
            symb_count = 1          
    compressed_str += str(symb_count) + txt[len(txt) - 1]
    return compressed_str

def rle_decompress(txt):
    decompressed_str = ''
    symb_count = ''
    for i in txt:
        for element in i:
            if element.isdigit():
                symb_count += element
            else:
                decompressed_str += element * int(symb_count)
                symb_count = ''
    return decompressed_str

compress_filename = 'hw5e4compress'
decompress_filename = 'hw5e4decompress'

create_txt_file(compress_filename)
# чтение из зарархивированного файла
with open(compress_filename, "r") as compressed_txt:
    compressed_str = compressed_txt.readlines()
#вывод строки из зархивированного файла
print(compressed_str)
# запись разархивированного файла
with open(decompress_filename, "w") as decompressed_txt:
    for element in compressed_str:
        decompressed_txt.writelines(rle_decompress(element))
#вывод строки из разархивированного файла
with open(decompress_filename, "r") as decompressed_txt:
    print(decompressed_txt.readlines())
