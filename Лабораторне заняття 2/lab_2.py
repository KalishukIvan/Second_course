import numpy as np

def task_1():

    def _app(lst_1, lst_2, n = 1):
        lst_1.extend(np.random.choice(lst_2,n))

    special_symbol = [i for i in "~!@#$%^&*()-_+=\/{}[].,?<>:;"]
    capital = [i for i in "ABCDEFGHIJKLMNOPQRSTUVWXYZ"]
    letters = [i.lower() for i in capital]
    numbers = [i for i in range(10)]
    password = []
    _app(password, special_symbol)
    _app(password, capital)
    _app(password, letters)
    _app(password, numbers)
    _app(password, special_symbol + capital + letters + numbers, 6)
    np.random.shuffle(password)
    res = ""
    for i in password:
        res += str(i)
    print("Random password -- {}".format(res))


if __name__ == '__main__':
    task_1()

