def bb(n):
    m = 1
    while (n != 1):
        if n % 2 == 0:
            n = n // 2
        else:
            n = n * 3 + 1
        if n > m:
            m = n
    return m

n = int(input())
m = 1
for i in range(1, n + 1):
    s = bb(i)
    if s > m:
        m = s
print(m)
