import numpy


def factorial(num):
    return numpy.prod([i+1 for i in range(num)])


num = input("Enter number:")
result = factorial(num)
print(result)
