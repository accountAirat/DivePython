from decimal import *

'''
Напишите программу банкомат.
✔ Начальная сумма равна нулю
✔ Допустимые действия: пополнить, снять, выйти
✔ Сумма пополнения и снятия кратны 50 у.е.
✔ Процент за снятие — 1.5% от суммы снятия, но не менее 30 и не более 600 у.е.
✔ После каждой третей операции пополнения или снятия начисляются проценты - 3%
✔ Нельзя снять больше, чем на счёте
✔ При превышении суммы в 5 млн, вычитать налог на богатство 10% перед каждой
операцией, даже ошибочной
✔ Любое действие выводит сумму денег
'''

getcontext().prec = 2

# Начальная сумма равна нулю
balance = 0

counter_completed_operation = 0
min_bill = 50

min_down_commission = 30
max_down_commission = 600
down_commission = 1.5 / 100  # 1.5%
operation_cashback = 3 / 100 # 3%

while True:
    # При превышении суммы в 5 млн, вычитать налог на богатство 10% перед каждой операцией, даже ошибочной
    if balance > 5_000_000:
        balance *= 0.9

    # Допустимые действия: пополнить, снять, выйти
    print('\tМеню'
          '\n1.Пополнить'
          '\n2.Снять'
          '\n0.Выйти')
    operation = input('Введите номер операции: ')

    match operation:
        # Операция пополнения
        case "1":
            money = int(input('Введите сумму пополнения (кратную 50 у.е.): '))
            if money % min_bill == 0 and money > 0:
                balance += money
                counter_completed_operation += 1
                print(f'Баланс успешно пополнен.\nБаланс: {balance}')
            else:
                print('Неверная сумма.')
        # Операция снятия
        case "2":
            money = int(input('Введите сумму снятия (кратную 50 у.е.): '))

            if money % min_bill == 0 and money > 0:
                # Процент за снятие — 1.5% от суммы снятия, но не менее 30 и не более 600 у.е.
                commission = money * down_commission
                if commission < min_down_commission:
                    commission = min_down_commission
                elif commission > max_down_commission:
                    commission = max_down_commission

                if (money + commission) < balance:
                    balance -= (money + commission)
                    counter_completed_operation += 1
                    print(f'Снятия наличных: {money}\nКомиссия: {commission}\nБаланс: {balance}')
                else:
                    print('На балансе недостаточно средств. Баланс: ', balance)  # Нельзя снять больше, чем на счёте
            else:
                print('Неверная сумма.')
        case "0":
            print('Пока! Баланс: ', balance)
            break
        case _:
            print('Неизвестная операция.')

    # После каждой третей операции пополнения или снятия начисляются проценты - 3%
    if counter_completed_operation == 3:
        counter_completed_operation = 0
        balance += (balance * operation_cashback)
        print('Начислен cashback за третью операцию! Баланс: ', balance)

