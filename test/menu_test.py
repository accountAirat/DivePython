from simple_term_menu import TerminalMenu

# menu = TerminalMenu(['Пополнить', 'Снять', 'Выйти'])
# print(f'{menu.show()}')


operations = {'Пополнить': 'a', 'Снять': 'b', 'Выйти': 'c'}
menu = TerminalMenu(operations)
print(f'{menu.show()}')