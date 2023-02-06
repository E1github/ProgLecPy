import os
import init as ii


def export_file(exp_type : str):
    path2base = ii.use_path+'/base.txt'
    with open(path2base, "r", encoding=ii.use_encoding) as file_original:
        path2file = ii.use_path+'/export/ver'+exp_type+'.txt'
        with open(path2file, "w", encoding=ii.use_encoding) as file_export:
            line_original = file_original.readline()
            while line_original:
                lst_export = line_original.split()
                if exp_type == '1':
                    line_export = str(lst_export[0] + '\n' + lst_export[1] + '\n' + lst_export[2] + '\n'  + lst_export[3] + '\n' + '\n')
                elif exp_type == '2':
                    line_export = str(lst_export[0] + ';' + lst_export[1] + ';' + lst_export[2] + ';' + lst_export[3] + '\n')    
                file_export.write(line_export)
                line_original = file_original.readline()
    return path2file
