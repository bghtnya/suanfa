n = 50

import math

p = [True] * (n + 1)
p[0] = p[1] = False
for i in range(2, int(math.sqrt(n)) + 1):
    if p[i]:
        for j in range(i * i, n + 1, i):
            p[j] = False

print([i for i,p in enumerate(p) if p])
