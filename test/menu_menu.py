import inquirer

questions = [
    inquirer.List('action',
                  message="Choose an action:",
                  choices=['Пополнить', 'Снять', 'Выйти'],
                  ),
]

answers = inquirer.prompt(questions)
print("You chose:", answers['action'])