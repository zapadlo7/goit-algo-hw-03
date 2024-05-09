import os
import shutil
import argparse

def copy_files(source_dir, destination_dir):
    # Рекурсивно копіює файли з вихідної директорії до призначеної
    for root, dirs, files in os.walk(source_dir):
        for file in files:
            # Отримуємо повний шлях до файлу
            source_path = os.path.join(root, file)
            # Отримуємо розширення файлу
            _, extension = os.path.splitext(file)
            # Створюємо піддиректорію на основі розширення
            dest_subdir = os.path.join(destination_dir, extension[1:])
            # Перевіряємо, чи існує піддиректорія, якщо ні - створюємо
            if not os.path.exists(dest_subdir):
                os.makedirs(dest_subdir)
            # Копіюємо файл у відповідну піддиректорію
            shutil.copy(source_path, dest_subdir)

def main():
    parser = argparse.ArgumentParser(description="Copy files recursively and sort them into directories based on their extensions")
    parser.add_argument("source_dir", help="Source directory path")
    parser.add_argument("destination_dir", nargs="?", default="dist", help="Destination directory path (default: dist)")
    args = parser.parse_args()

    # Перевіряємо, чи існує вихідна директорія
    if not os.path.exists(args.source_dir):
        print(f"Source directory '{args.source_dir}' does not exist.")
        return

    # Перевіряємо, чи існує директорія призначення, якщо ні - створюємо
    if not os.path.exists(args.destination_dir):
        os.makedirs(args.destination_dir)

    # Викликаємо функцію копіювання файлів
    copy_files(args.source_dir, args.destination_dir)

if __name__ == "__main__":
    main()