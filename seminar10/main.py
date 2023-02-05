import telebot
from telebot import types

flag = 'X'
data = {1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7', 8: '8', 9: '9'}
end_game = False

bot = telebot.TeleBot("5476492755:AAFZgt5w3WTZOC8Nzh9556qkOroWBtQwl7I")

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




@bot.message_handler(commands=['start']) # вызов функции по команде в списке
def controller(message):
    global flag    
    bot.send_message(message.chat.id,
                     f"Введите номер поля: ")  # отправка сообщения (кому отправляем, что отправляем(str))
    bot.register_next_step_handler(message, user_input)

       
def get_count(message):
    global sweets
    sweets = sweets - user_sweets
    bot.send_message(message.chat.id, f"осталось {sweets}")
    controller(message)

def user_input(message):
    global user_sweets
    user_sweets = int(message.text)
    get_count(message)

bot.infinity_polling()

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
