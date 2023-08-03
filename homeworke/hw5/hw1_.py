import os

def split_path(path: str) -> tuple[str]:
    return os.path.split(path), *os.path.split(path)[-1].split('.')


absolute_path = r'C:\Users\Айрат\PicturesСкриншотер\Скриншот.jpg'

print(split_path(absolute_path))

