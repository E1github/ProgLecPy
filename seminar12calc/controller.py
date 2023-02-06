import user_interface as ui
import log_generate as lg
import model_racional as mr


def start_nums():
    user_nums, nums = ui.get_n()  # Получение данных от пользователя
    print(user_nums)
    print(nums)
    # lg.write_data(f'Ввод пользователя: {user_nums}')  # Запись данных которые ввел пользователь в лог
    result = mr.get_result(nums)  # Решаем пример
    # lg.write_data('Итоговый результат: ' + user_nums + ' = ' + result)  # Запись результата в лог
    # lg.write_data('')  # Добавляем пустую строку-разделитель в логе между разными примерами
    ui.print_user(user_nums, result)  # Вывод результата пользователю в терминал
    # print('Содержимое лог-файла:')
    # lg.read_log()  # Вывод в консоль содержимого лог-файла