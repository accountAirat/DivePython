import os
from pathlib import Path

print(os.getcwd())
print(Path.cwd())

os.chdir('../..')
print(os.getcwd())
print(Path.cwd())

os.mkdir('new_os_dir')
Path('new_path_dir').mkdir()

os.makedirs('dir/new_os_dir')  # Если каталоги уже есть, выдаст ошибку.
Path('new_path_dir').mkdir(parents=True)  # Если каталоги уже есть, выдаст ошибку.


os.rmdir('new_os_dir')
Path('new_path_dir')

