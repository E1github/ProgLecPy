import os
import init as ii
# from main import init as initz

def create_base():
    # initz()
    global use_path
    global use_encoding
    if not os.path.exists(use_path+'/base.txt'):
        temp = open(use_path+'/base.txt', "w", encoding=use_encoding)
        # temp.writelines(first_line)
        temp.close()
    else:
        temp = []
        with open(use_path+'/base.txt', "r", encoding=use_encoding) as file:
            for line_num, line in enumerate(file, start=1):
                temp.append(str(line_num) + '. ' + line[:(-1)])
        return line_num, temp    

def show_contacts():
    temp_lst = []
    with open(''+ii.use_path+'/base.txt', "r", encoding=ii.use_encoding) as file:
        for line_numb, line in enumerate(file, start=1):
            temp_lst.append(str(line_numb) + '. ' + line[:(-1)])
    return line_numb, temp_lst

def add_contact(add_str):
    with open(''+ii.use_path+'/base.txt', "a", encoding=ii.use_encoding) as file:
        return file.write(add_str)
            
def find_contacts(find_str = str):
    result_find = []
    with open(''+ii.use_path+'/base.txt', "r", encoding=ii.use_encoding) as file:
        for line_numb, line in enumerate(file, start=1):
            if find_str in line:
                result_find.append(line[:(-1)])
    return result_find