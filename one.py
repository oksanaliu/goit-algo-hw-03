import os
import shutil
import argparse

def parse_arguments():
    parser = argparse.ArgumentParser(description='Рекурсивне копіювання та сортування файлів за розширенням.')
    parser.add_argument('src_dir', nargs='?', default=None, help='Вихідна директорія')
    parser.add_argument('dst_dir', nargs='?', default='dist', help='Директорія призначення ')
    return parser.parse_args()

def copy_files(src_dir, dst_dir):
    # Рекурсивно обходимо директорії та копіюємо файли
    for root, dirs, files in os.walk(src_dir):
        for file in files:
            file_path = os.path.join(root, file)
            file_extension = os.path.splitext(file)[1].lstrip('.').lower() or 'no_extension'
            dest_dir = os.path.join(dst_dir, file_extension)
            os.makedirs(dest_dir, exist_ok=True)  # Створюємо піддиректорію для копіювання файлу
            try:
                shutil.copy(file_path, dest_dir)  # Копіюємо файл у відповідну піддиректорію
                print(f'Скопійовано {file_path} до {dest_dir}')
            except Exception as e:
                print(f'Помилка копіювання {file_path}: {e}')

def main():
    args = parse_arguments()
    
    # Встановлюємо вихідну та призначену директорії з аргументів командного рядка
    src_dir = args.src_dir if args.src_dir else '/Users/oksanaluklan/goit-algo-hw-03/source' 
    dst_dir = args.dst_dir
    
    # Перевіряємо існування вихідної директорії або створюємо її, якщо вона відсутня
    if not os.path.exists(src_dir):
        try:
            os.makedirs(src_dir)  
            print(f'Створено вихідну директорію {src_dir}')
        except Exception as e:
            print(f'Не вдалося створити вихідну директорію {src_dir}: {e}')
            return

    # Створюємо основну директорію призначення
    os.makedirs(dst_dir, exist_ok=True)
    
    # Викликаємо функцію для копіювання файлів
    copy_files(src_dir, dst_dir)
    
    print('Копіювання та сортування файлів завершено.')

if __name__ == '__main__':
    main()