import math
n = int(input())
l = {}

for _ in range(n):
    s, x, y = input().split()
    l[s] = (int(x), int(y))

m = int(input())

for _ in range(m):
    a, b = input().split()
    x1, y1 = l[a]
    x2, y2 = l[b]

    dis = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    print(f"{dis:.2f}")
