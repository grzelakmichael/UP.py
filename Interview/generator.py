def fib():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b


a = fib()

for i in range(10):
    print(next(a))


class fib2(object):
    def __init__(self):
        self.a, self.b = 0, 1

    def __iter__(self):
        return self

    def __next__(self):
        return self.next()

    def next(self):
        self.a, self.b = self.b, self.a + self.b


b = fib2()
for i in range(10):
    print(next(b))
