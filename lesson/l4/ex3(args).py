def mean(*args):  # *args создаёт кортеж
    return sum(args) / len(args)


print(mean(*[1, 2, 3]))
print(mean(1, 2, 3))
