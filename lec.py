# a = int(input('Введите а: ')) # 11
# b = int(input('Введите b: ')) # 22
# c = 33
# print('{} + {} = {}'.format(a, b, c)) # 11 + 22 = 33111

# exp1 = 2**3 - 10 % 5 + 2*3
# exp2 = (2**3) - (10 / 5) + (2*3)1
# print(exp1) # 14.0 или 14
# print(exp2) # 12.0 или 12

# a, b, c = 1, 2, 3
# # a: 1 b: 2 c: 3
# print('a: {} b: {} c: {}'.format(a, b, c))
# print(range(*(1,5,2)))

# username = input('Введите имя: ')
# if username == 'Маша':
#     print('Ура, это же МАША!')
# elif username == 'Марина':
#     print('Я так ждала Вас, Марина!')
# elif username == 'Ильнар':
#     print('Ильнар - топ)')
# elif username == 'E1':
#     print('Yeep)')    
# else:
#     print('Привет, ', username)

# original = int(input('Введите: ')) 
# inverted = 0
# while original != 0:
#     inverted = inverted * 10 + (original % 10)
#     original //= 10
# print(inverted)

# for i in 1, -2, 3, 14, 5:
#     print(i)
    
# line = "="
# for i in range(5):
#     line += "-"
#     for j in range(5):
#         line += "*"
# print(line)

# text = 'съешь ещё этих мягких французских булок'
# print(len(text)) # 39
# print('ещё' in text) # True
# print(text.isdigit()) # False
# print(text.islower()) # True
# print(text.replace('ещё','ЕЩЁ')) #
# # for c in text:                                              #???
# #     print(c)
# print(text[0]) # c
# print(text[1]) # ъ
# print(text[len(text)-1]) # к
# print(text[-5]) # б
# print(text[:]) # print(text)
# print(text[:2]) # съ
# print(text[len(text)-2:]) # ок
# print(text[2:9]) # ешь ещё
# print(text[6:-18]) # ещё этих мягких
# print(text[0:len(text):6]) # сеикакл
# print(text[::6]) # сеикакл
# text = text[2:9] + ' ' + text[-5] + ' ' + text[:2] # .
# print(text)


# colors = ['red', 'green', 'blue']
# for e in colors:
#     print(e) # red green blue
# print(colors[0], colors[1], colors[2])
# for e in colors:
#     print(e*2) # redred greengreen blueblue
# colors.append('gray') # добавить в конец
# print(colors == ['red', 'green', 'blue', 'gray']) # True
# colors.remove('red') #del colors[0] # удалить элемент


# def f(x):
#     return x**2

x = input('Введите: ')
def f(x):
    if x == 1:
        return 'Целое'
    elif x == 2.3:
        return 23
    else:
        return
print(f(x)) # None
print(type(f(x))) # str