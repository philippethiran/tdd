def another_sum(a, b):
    return a + b


def add_10(a):
    return a + 10


def add_series(a, b):
    y = 0
    for x in range(a, b + 1):
        y = y + x
    return y


def add_even_series(a, b):
    # this function add only the even numbers between a and b
    y = 0
    if (a % 2) != 0:  # a is not even
        a = a + 1      # we start then with the first pair after a
    for x in range(a, b+1, 2):
        y = y + x
    return y
