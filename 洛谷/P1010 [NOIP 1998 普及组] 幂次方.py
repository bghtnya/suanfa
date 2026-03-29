import math

n = int(input())


def deal(n):
    a = ''
    while n != 0:
        q = int(math.log2(n))
        n -= 2 ** q
        if q == 1:
            a += '2+'
            continue
        if q > 2: q = deal(q)
        a += f'2({q})+'
    return a[:-1]


print(deal(n))
