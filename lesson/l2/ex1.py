#1
DEFAULT = 42
num = int(input('Введите уроверь или 0 для значения по умолчанию: '))
level = num or DEFAULT
print(level)

#2
name = input('Как вас зовут? ')
if name:
    print('Привет, ' + name)
else:
    print('Анонимус, приветствую')
#3
data = [0, 1, 2 ]
while data:
    print(data.pop())