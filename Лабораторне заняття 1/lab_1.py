from itertools import permutations, combinations, combinations_with_replacement, product



def task_1_3():
    elements = [{1, 3, 5}, {1, 2, 3, 4}, {1, 2, 2, 1}, {1, 2, 3, 4, 5}, {1, 2, 3, 4, 5, 6, 7}, {1, 3, 5, 7, 9, 11, 13, 15, 17, 19}]
    for element in elements:
        permut = set(permutations(element))
        print("Permutations of {} : {}".format(element, permut))
        print("Number of permutations - {}".format(len(permut)))


def task_1_4():
    def _test(element, p):
        for i in range(len(element)):
            if element[i] == p[i]:
                return False
        return True

    elements = [[1, 2, 3], [1, 2, 3, 4], [1, 3, 5, 7], [1, 2, 2, 1]]
    for element in elements:
        permut = set(permutations(element))
        res = []
        for p in permut:
            if _test(element, p):
                res.append(p)
        print("Permutations of {} without stable elements -- {}".format(element,res))
        print("It's number is -- {}".format(len(res)))


def task_1_5():
    def _test(p):
        tmp = list(p)
        for i in range(0,3):
            if tmp[i] > tmp[i+1]:
                return False
        for i in range(4,len(tmp)):
            if tmp[i-1] < tmp[i]:
                return False
        return True

    elements = [{1, 2, 3, 4, 5, 6, 7, 8}, {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}]
    for element in elements:
        permut = set(permutations(element))
        res = []
        for p in permut:
            if _test(p):
                res.append(p)
        print("Good permutations of {} -- {}".format(element, res))
        print("It's number is -- {}".format(len(res)))


def task_2_1():
    elements = [(4,2), (4,3), (5,2), (6,2), (6,4), (8,4)]
    for element in elements:
        tmp = [i+1 for i in range(element[0])]
        permut = set(permutations(tmp,element[1]))
        print("Permutations of {} by {} -- {}".format(tmp,element[1],permut))
        print("It's number is -- {}".format(len(permut)))


def task_3_1():
    elements = [(4, 2), (4, 3), (5, 2), (6, 2), (6, 4), (8, 4)]
    for element in elements:
        tmp = [i + 1 for i in range(element[0])]
        permut = set(combinations(tmp, element[1]))
        print("Permutations of {} by {} -- {}".format(tmp, element[1], permut))
        print("It's number is -- {}".format(len(permut)))


def task_3_2(mode):
    """
    Choose which way you want to go: stupid or more intelligent
    :param mode:
    :return:
    """
    if mode == "stupid":
        import random
        A = [random.randrange(0,26) for i in range(10)]
        B = list(map(sum, combinations(A,2)))
        print("All possible sums -- {}".format(B))
        print("It's number is -- {}".format(len(B)))

    elif mode == "clever":
        from math import factorial
        print("It's number is -- {}".format(factorial(10)/(factorial(8)*2)))

    else:
        print("Choose your way, son")
        way = input("Your way: ")
        task_3_2(way)

def task_4_2():
    elements = [(4, 2), (4, 3), (5, 2), (6, 2), (6, 4), (8, 4)]
    for element in elements:
        tmp = [i + 1 for i in range(element[0])]
        permut = set(combinations_with_replacement(tmp, element[1]))
        print("Permutations of {} by {} -- {}".format(tmp, element[1], permut))
        print("It's number is -- {}".format(len(permut)))


def task_5_1():
    def _test(number):
        if sum(number[:3]) == sum(number[3:]):
            return True
        return False

    a = [i for i in range(10)]
    numbers = set(product(a,repeat = 6))
    res = []
    for number in numbers:
        if _test(number):
            res.append(number)
    print("Number -- {}".format(len(res)))


def task_5_2():
    def _test(number):
        for i in range(len(number)-1):
            if number[i] == number[i+1]:
                return False
        return True

    a = [i for i in range(10)]
    numbers = set(product(a,repeat = 6))
    res = []
    for number in numbers:
        if _test(number):
            res.append(number)
    print("Number -- {}".format(len(res)))


if __name__ == '__main__':
    #task_1_3()
    #task_1_4()
    #task_1_5()
    #task_2_1()
    #task_3_1()
    #task_4_2()
    task_5_1()
    #task_5_2()
    pass
