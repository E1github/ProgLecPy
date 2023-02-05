import os
import init as ii
# from interface import print_blue as print_blue
# from interface import print_red as print_red

def import_file(imp_type : str):
    path2file = ii.use_path+'/import/file'+imp_type+'.txt'
    if os.path.exists(path2file):
        with open(path2file, 'r', encoding=ii.use_encoding) as file:
            line_temp = file.readlines()
            print(line_temp)
            print(type(line_temp))
            if imp_type in ['1']:
            # if str(line_temp[0]).find('*') != -1:
                import_dict_1(line_temp)
            elif imp_type in ['2']:
                import_dict_2(line_temp)
    else:
        print('Импортируемый файл должен находиться в каталоге ', end='')
        print(ii.use_path)

def import_dict_1(import_line):
    path2base = ii.use_path+'/base.txt'
    str_imp_line = ''
    for i in range(len(import_line)):
        str_imp_line += ' '.join(import_line[i][:-1].split(' ')) + '\n'
    with open(path2base, 'a', encoding=ii.use_encoding) as file_dict:
        file_dict.write(str_imp_line)
    print("\033[34m{}".format('Данные загружены'))
    print('\033[37m{}'.format(''), end='')
    return

def import_dict_2(import_line):
    path2base = ii.use_path+'/base.txt'
    str_imp_line = ''
    for i in range(len(import_line)):
        str_imp_line += ' '.join(import_line[i][:-1].split(';')) + '\n'
    with open(path2base, 'a', encoding=ii.use_encoding) as file_dict:
        file_dict.write(str_imp_line)
    print("\033[34m{}".format('Данные загружены'))
    print('\033[37m{}'.format(''), end='')
    return