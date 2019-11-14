import math


def f1(x):
    return 6 + 2 * x[0]


def f2(x):
    return 6 + 2 * x[1]


def df1dx1(x1, x2):
    return 4.5 * pow(x1, 2)


def df1dx2(x1, x2):
    return -2 * x2


def df2dx1(x1, x2):
    return pow(x2, 3)


def df2dx2(x1, x2):
    return 3 * x1 * pow(x2, 2)


def f3(x):
    return math.sin(x)

