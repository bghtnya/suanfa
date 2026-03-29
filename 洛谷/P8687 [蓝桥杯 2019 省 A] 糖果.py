n, m, k = map(int, input().split())
t = []
for i in range(n):
    tp = list(map(int, input().split()))
    t.append(tp)


def check(ts):
    ts=sum(ts,[])
    for i in range(1, m + 1):
        if i not in ts:
            return False
    return True


if check(t) == False:
    print(-1)
    exit(0)

import itertools

for i in range(1, n + 1):
    for tb in itertools.combinations(t, i):
        if check(list(tb)):
            print(i)
            exit(0)
