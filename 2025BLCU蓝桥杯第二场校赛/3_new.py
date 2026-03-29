n, k = map(int, input().split())
a = [tuple(map(int, input().split())) for _ in range(n)]

def check(x):
    return sum((h // x) * (w // x) for h, w in a) >= k

l, r, ans = 1, 100000, 1
while l <= r:
    m = (l + r) // 2
    if check(m):
        ans = m
        l = m + 1
    else:
        r = m - 1

print(ans)
