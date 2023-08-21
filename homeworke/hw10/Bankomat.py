import inquirer

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

"""
Возьмите 1-3 любые задания из прошлых семинаров (например сериализация данных), которые вы уже решали.
Превратите функции в методы класса, а параметры в свойства.
Задания должны решаться через вызов методов экземпляра.
"""


class Bankomat:
    __balance = 0
    counter_completed_operation = 0

    def __init__(self, min_take=50, min_take_commission=30, max_take_commission=600,
                 down_commission=(1.5 / 100), operation_cashback=(3 / 100)):
        self.min_take = min_take
        self.min_take_commission = min_take_commission
        self.max_take_commission = max_take_commission
        self.down_commission = down_commission  # 1.5%
        self.operation_cashback = operation_cashback  # 3%

    def start(self):
        """
        Допустимые действия: пополнить, снять, выйти
        :return:
        """
        while True:
            operations = {'Пополнить': self.add, 'Снять': self.take, 'Выйти': self.finish}
            questions = [inquirer.List('action', message=f"Меню", choices=operations,),]
            answers = inquirer.prompt(questions)
            operations[answers['action']]()

    def finish(self):
        print('Пока! Баланс: ', self.__balance)
        exit()

    def check_for_rich(self):
        """
        При превышении суммы в 5 млн, вычитать налог на богатство 10% перед каждой операцией, даже ошибочной
        :return:
        """
        if self.__balance > 5_000_000:
            summ = self.__balance * 0.1
            self.__balance -= summ
            print(f'Снят процент на роскаш! Комиссия: {summ} Баланс: {self.__balance}')

    def check_cashback(self):
        """
        После каждой третей операции пополнения или снятия начисляются проценты - 3%
        :return:
        """
        if self.counter_completed_operation == 3:
            self.counter_completed_operation = 0
            summ = self.__balance * self.operation_cashback
            self.__balance += summ
            print(f'Начислен cashback за третью операцию! Сashback: {summ} Баланс: ', self.__balance)

    def add(self):
        """
        Операция пополнения баланса
        :return:
        """
        self.check_for_rich()
        money = int(input(f'Введите сумму пополнения (кратную {self.min_take} у.е.): '))
        if money % self.min_take == 0 and money > 0:
            self.__balance += money
            self.counter_completed_operation += 1
            print(f'Баланс успешно пополнен.\nБаланс: {self.__balance}')
            self.check_cashback()
        else:
            print('Неверная сумма.')
        

    def take(self):
        """
        Операция снятия с баланса
        :return:
        """
        self.check_for_rich()

        money = int(input('Введите сумму снятия (кратную 50 у.е.): '))

        if money % self.min_take == 0 and money > 0:
            # Процент за снятие — 1.5% от суммы снятия, но не менее 30 и не более 600 у.е.
            commission = money * self.down_commission
            if commission < self.min_take_commission:
                commission = self.min_take_commission
            elif commission > self.max_take_commission:
                commission = self.max_take_commission

            if (money + commission) < self.__balance:
                self.__balance -= (money + commission)
                self.counter_completed_operation += 1
                print(f'Снятия наличных: {money}\nКомиссия: {commission}\nБаланс: {self.__balance}')
                self.check_cashback()
            else:
                print('На балансе недостаточно средств. Баланс: ', self.__balance)  # Нельзя снять больше, чем на счёте
        else:
            print('Неверная сумма.')


if __name__ == '__main__':
    atm = Bankomat()
    atm.start()

