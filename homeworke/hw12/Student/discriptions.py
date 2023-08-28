class Name:
    def __init__(self):
        pass

    def __set_name__(self, owner, name):
        self.param_name = f"_{name}"

    def __get__(self, instance, owner):
        return getattr(instance, self.param_name)

    def __set__(self, instance, value):
        self.check(value)
        setattr(instance, self.param_name, value)

    def check(self, value: str):
        if value.isalpha() and value.istitle():
            return True
        raise ValueError('ФИО должно состоять только из букв и первая должна быть заглавной.')


class Range:
    pass