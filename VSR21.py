# Задание ВСР 2
#
# 2.1. Разработать функцию, возвращающую список чисел ряда Фибоначчи
# с использованием бесконечных итераторов (модуль itertools).

import itertools

def fib():
    a, b = 1, 1
    while True:
        yield a
        a, b = b, a + b

n = int(input())
f = []

for i in itertools.takewhile(lambda x: x < n, fib()):
    f.append(i)

print(f)