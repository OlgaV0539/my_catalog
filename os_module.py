import os
import time

directory = 'C:/Python/pythonProject4'
for root, dirs, files in os.walk(directory):
    print(f'Текущий каталог: {root}')
    print('Подкаталоги:')
    for dirname in dirs:
        print(f' - {dirname}')

    print('Файлы:')
    for file in files:
        filepath = os.path.join(root, file)
        filetime = os.path.getmtime(filepath)
        formatted_time = time.strftime("%d.%m.%Y %H:%M", time.localtime(filetime))
        file_size = os.path.getsize(filepath)
        parent_dir = os.path.dirname(filepath)
        print(f'Обнаружен файл: {file}, Путь: {filepath}, Размер: {file_size} байт,'
              f' Время изменения: {formatted_time}, Родительская директория: {parent_dir}')
    print()
