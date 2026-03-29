n, k = map(int, input().split())

def isluckkynum(n):
    s = str(n)
    return all(c in '47' for c in s)


import itertools

data = list(itertools.permutations(list(range(1, n + 1))))
data.sort()
if k - 1 > len(data):
    print(-1)
    exit(0)
data = data[k - 1]
s = 0

for i in range(1, 1 + len(data)):

    if isluckkynum(i):
        if isluckkynum(data[i - 1]):
            s += 1
print(s)


