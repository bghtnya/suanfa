m, k = map(int, input().split())
ans = 0
if m % 2 == 0:
    if k == m:
        ans = 0
    else:
        ans = (m - 1 - k) // 2 + 1 - max(m // 2 - k, 0)
else:
    if k == m:
        ans = 1
    elif k == m - 1:
        ans = 0
    else:
        ans = (m - 2 - k) // 2 + 1 - max(m // 2 - k, 0)
print(ans)
