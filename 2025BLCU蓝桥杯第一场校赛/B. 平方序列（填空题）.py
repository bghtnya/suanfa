import math


for x in range(1428, 10 ** 9):
    y = int(math.sqrt(2 * x * x - 2019 ** 2))
    if y ** 2 == 2 * x * x - 2019 ** 2:
        if 2019<x<y:
            print(x, y, x + y)
