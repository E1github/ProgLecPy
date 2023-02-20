import log_generate as lg
import logging


def calc(my_list):  # Функция решения арифметических действий
    while '*' in my_list or '/' in my_list:
        for i in range(1, len(my_list), 2):
            if my_list[i] == '*':
                result = my_list.pop(i + 1) * my_list.pop(i - 1)
                my_list[i - 1] = result
                break
            elif my_list[i] == '/':
                try:
                    logging.info(f"Trying divizion {my_list[i-1]} / {my_list[i+1]}.")
                    result = my_list.pop(i - 1) / my_list.pop(i)
                    my_list[i - 1] = result
                except ZeroDivisionError as err:
                    logging.error("ZeroDivisionError",exc_info=True)
                break

    while '+' in my_list or '-' in my_list:
        for i in range(1, len(my_list), 2):
            if my_list[i] == '-':
                result = my_list.pop(i - 1) - my_list.pop(i)
                my_list[i - 1] = result
                break
            elif my_list[i] == '+':
                result = my_list.pop(i + 1) + my_list.pop(i - 1)
                my_list[i - 1] = result
                break

    return my_list


def get_result(data):
    # lg.write_data(f'Пример подготовленный для решения: {data}')
    while '(' in data:  # Открытие скобок если они имеются
        first_i = len(data) - data[::-1].index('(') - 1
        second_i = first_i + data[first_i + 1:].index(')') + 1
        data = data[:first_i] + calc(data[first_i + 1:second_i]) + data[second_i + 1:]
    
        # lg.write_data(f'Результат открытия скобок: {data}')
    data = calc(data)  # Вызов функции calc() после открытия скобок
    return ''.join(map(str, data))