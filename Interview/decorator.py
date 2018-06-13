def dec(arg):
    def real_decorator(f):
        def wrapper(*args):
            print('Hello World')
            f(arg, *args)
        return wrapper
    return real_decorator

@dec('dwa')
def printer(*par):
    print(*par)

printer('cos')