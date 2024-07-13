import os
import shutil
import argparse

def parse_arguments():
    parser = argparse.ArgumentParser(description='Рекурсивне копіювання та сортування файлів за розширенням.')
    parser.add_argument('src_dir', help='Вихідна директорія')
    parser.add_argument('dst_dir', nargs='?', default='dist', help='Директорія призначення (за замовчуванням "dist")')
    return parser.parse_args()

def copy_files(src_dir, dst_dir):
    # Перевірка чи src_dir є директорією
    if not os.path.isdir(src_dir):
        print(f'{src_dir} не є директорією')
        return

    # Перебір всіх елементів у директорії
    for item in os.listdir(src_dir):
        src_path = os.path.join(src_dir, item)
        if os.path.isdir(src_path):
            # Якщо елемент є директорією, викликаємо функцію рекурсивно
            new_dst_dir = os.path.join(dst_dir, item)
            os.makedirs(new_dst_dir, exist_ok=True)
            copy_files(src_path, new_dst_dir)
        else:
            # Якщо елемент є файлом, копіюємо його
            file_extension = os.path.splitext(item)[1].lstrip('.').lower() or 'no_extension'
            dest_dir = os.path.join(dst_dir, file_extension)
            os.makedirs(dest_dir, exist_ok=True)
            try:
                shutil.copy(src_path, dest_dir)
                print(f'Скопійовано {src_path} до {dest_dir}')
            except Exception as e:
                print(f'Помилка копіювання {src_path}: {e}')

def main():
    args = parse_arguments()
    src_dir = args.src_dir
    dst_dir = args.dst_dir

    if not os.path.exists(src_dir):
        print(f'Вихідна директорія {src_dir} не існує.')
        return

    os.makedirs(dst_dir, exist_ok=True)
    copy_files(src_dir, dst_dir)
    print('Копіювання та сортування файлів завершено.')

if __name__ == '__main__':
    main()