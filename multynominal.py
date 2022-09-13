# https://stepik.org/lesson/512854/step/16?unit=505068 (module 15.8 step 16)

from functools import reduce

def evaluate(coeficients, x):
    levels = [int(i) for i in range(len(coeficients) - 1, -1, -1)]
    multinominal = map(lambda num, level: num * x ** level, coeficients, levels)
    result = reduce(lambda z, y: z + y, multinominal, 0)
    return result


coeficients = [int(i) for i in input().split()]
x = int(input())

print(evaluate(coeficients, x))
