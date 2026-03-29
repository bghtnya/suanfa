def avg(n, l):
    c = []
    for i in range(n + 1):
        for j in range(i + 1, n + 1):
            c.append(sum(l[i:j]) // (j - i))
    return max(c)


t = int(input())
for _ in range(t):
    n = int(input())
    l = list(map(int, input().split()))
    print(avg(n, l))
