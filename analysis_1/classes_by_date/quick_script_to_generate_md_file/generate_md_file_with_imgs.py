'''

    yeah, has a lot hardcoded, was done in minutes, don't judge

'''

import os
import sys
import shutil
import pathlib

if __name__ == '__main__':
    if len(sys.argv) == 2:
        
        date_folder_path :str = sys.argv[1]
        file_list :list[str] = os.listdir(date_folder_path)
        img_folder_path :str = os.path.join(date_folder_path,'imgs')
        md_file_path :str = os.path.join(date_folder_path, (pathlib.Path(date_folder_path).name + '_md_file_w_images.md'))


        # move everything to the imgs folder and fix the windows (x) numering system to _x, ít's expected that the src folder will only have imgs for now
        
        os.mkdir(os.path.join(date_folder_path,'imgs'))
        aux_new_file_list: list[str] = []
        for i in file_list:
            shutil.move(os.path.join(date_folder_path,i), img_folder_path)
            aux_i = i.replace(' (', '_').replace(')','')
            os.rename(os.path.join(img_folder_path,i), os.path.join(img_folder_path,aux_i))
            aux_new_file_list.append(aux_i)

        aux_new_file_list.sort(key = lambda i: int(i.split('_')[-1].split('.')[0]))

        file_list = aux_new_file_list

        with open(md_file_path, 'w') as f:
            for i in file_list:
                f.write('![' + i + '](imgs/' + i + ')\n')