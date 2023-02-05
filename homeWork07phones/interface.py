# from main import init as inits
# 
import init as ii
import data_import as di
import data_export as de
import data_manage as dm

def print_blue(text):
    print('\033[34m{}'.format(text))
    print('\033[37m{}'.format(''), end='')
    
def print_red(text):
    print('\033[31m{}'.format(text))
    print('\033[37m{}'.format(''), end='')

def main_menu():
    var_choice = ['1', '2', '3', '4', '0']
    print('>>Выберите действие \n================ \n 1 -просмотр базы телефонов\n 2 -ввод контакта\n 3 -импорт контактов\n 4 -экспорт контактов\n 0 -выход')
    choice = input('================> ')
    if choice in var_choice:
        if choice == '0':
            print_red('\nРабота справочника завершена')
            exit()
        elif choice == '1':
            print_blue(f'Количество записей в базе: {dm.show_contacts()[0]}\nСписок записей:\n{dm.show_contacts()[1]}')
            print('Для поиска по базе введите строку или Enter для выхода: ')
            find_string = str(input('=> '))
            if find_string != '':
                print_blue(f'Результат поиска:\n{dm.find_contacts(find_string)}')
            main_menu()
        elif choice == '2':
            add_menu()    
        elif choice == '3':
            import_menu()
        elif choice == '4':
            export_menu()
    else:
        print_red('Вы ввели не корректное значение: ' + choice)
        main_menu()
    
def import_menu():
    var_choice = ['1', '2', '0']
    print('>>Импортировать данные из файла с разделителями\n================ \n 1 -пробелы (" ") \n 2 -точка с запятой (";")\n 0 -выход')
    choice = input('================> ')
    if choice in var_choice:
        if choice == '0':
            main_menu()
        elif choice in ['1','2']:
            di.import_file(choice)
    else:
        print_red('Вы ввели не корректное значение: ' + choice)
    import_menu()

def export_menu():
    var_choice = ['1', '2', '0']
    print('>>Экспортировать данные из базы в формате\n================ \n 1 -вертикальном\n 2 -горизонтальном (разделитель запятая ",")\n 0 -выход')
    choice = input('================> ')
    if choice in var_choice:
        if choice == '0':
            main_menu()
        else:
            print('Данные экспортированы в файл: ', end='')
            print_blue(de.export_main(choice))
            export_menu()      
        # elif choice == '1':
        #     de.exportV1()
        # elif choice == '2':
        #     de.exportV2()
    else:
        print_red('Вы ввели не корректное значение: ' + choice)
        export_menu()

def add_menu():
    print('>>Добавление контакта в базу\n================')
    add_str = (input(f'Введите номер  => ') + ' ' +
            input(f'Введите имя => ') + ' ' +
            input(f'Введите фамилию => ') + ' ' +
            input(f'Введите примечание => ') + '\n')
    # print(add_str)
    if dm.add_contact(add_str):
        print_blue('===============\n...запись сохранена...\n===============')
    else:
        print_red('===============\n...ошибка записи...\n===============')
    main_menu()