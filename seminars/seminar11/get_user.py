import time
from getpass import getuser


class MyString(str):
    def __new__(cls, *args, **kwargs):
        instance = super().__new__(cls, *args, **kwargs)
        instance.name = getuser()
        instance.time_val = time.time()
        return instance

    def __init__(self, str_val):
        self.str_val = str_val

print(MyString('sadd').name)