class Factorial:
    def __init__(self, start, stop=None, step=1):
        self.start = start
        self.stop = stop
        self.step = step
        if stop is None:
            self.stop = start
            self.start = 1
        self.value = 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.start <= self.stop:
            self.value *= self.start
            self.start += self.step
            return self.value
        raise StopIteration


factorial = Factorial(1, 7)

print(*factorial)
