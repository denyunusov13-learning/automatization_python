import math


def square(side):
    return side * side


side = float(input("Введите длину стороны: "))
print(math.ceil(square(side)))
