def get_n(user_nums):  # Получение данных от пользователя
    # user_nums = input('Введите пример: ')
    nums = user_nums.replace('+', ' + ') \
        .replace('-', ' - ') \
        .replace('*', ' * ') \
        .replace('/', ' / ') \
        .replace('(', '( ') \
        .replace(')', ' )') \
        .replace('i', 'j') \
        .split()
    nums_list = list()
    for el in nums:
        if 'j' in el:
            nums_list.append(complex(el))
        elif el.isdigit():
            nums_list.append(int(el))
        else:
            nums_list.append(el)
    return nums_list
# user_nums, 

def print_user(nums, data):  # Вывод данных пользователю
    print('{}={}'.format(nums, data))