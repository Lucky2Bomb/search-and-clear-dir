import os
import shutil

dir_for_rmtree = 'testdir — копия (16)'
main_path = 'C:\\root_dir'
main_dir = os.listdir(main_path)
if(os.path.isdir(f'{main_path}\{dir_for_rmtree}')):
    print('папка для очищения', dir_for_rmtree)
    print('директория', main_path)


    if dir_for_rmtree in main_dir:
        path_dir_for_rmtree = f"{main_path}\{dir_for_rmtree}"
        shutil.rmtree(path_dir_for_rmtree)

    print(dir_for_rmtree, 'очищена')
else:
    print(dir_for_rmtree, 'не существует или не является папкой!')