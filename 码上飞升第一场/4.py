m, k = map(int, input().split())
l = max((m + 2) // 2, m - k + 1)
r = m - (k // 2)
print(max(0, r - l + 1))
