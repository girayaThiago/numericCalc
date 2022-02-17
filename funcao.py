import math

def f1(x):
    return x**4 - x**3 + x*math.sin(x) -1

def f2(x):
    return math.cos(x) - x**3

def phif2(x):
    return math.cos(x)**(1/3)

def f3(x):
    return math.e**x + math.sin(x)

def df3(x):
    return math.e**x + math.cos(x)