import shutil

shutil.rmtree('dir/new_os_dir')  # dic останется
shutil.rmtree('dir')  # Удалиться всё

shutil.copy('one.txt', 'dir')
shutil.copy2('two.txt', 'dir')

shutil.copytree('dir', 'one_more_dir')