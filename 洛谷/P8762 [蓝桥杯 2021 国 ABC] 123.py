import math

def getnum(w):
    i = (math.isqrt(1 + 8 * w) - 1) // 2
    s = i * (i + 1) // 2
    if s < w:
        i += 1
        s = i * (i + 1) // 2
    return w - s + i, i

def sum_r(a, b):
    return (a + b) * (b - a + 1) // 2

def tsum(k):
    return k * (k + 1) * (k + 2) // 6


n = int(input())
for _ in range(n):
    l, r = map(int, input().split())
    nl, il = getnum(l)
    nr, ir = getnum(r)
    if il == ir:
        s = sum_r(nl, nr)
    else:
        s = tsum(ir - 1) - tsum(il)
        s += sum_r(nl, il)
        s += sum_r(1, nr)

    print(s)
