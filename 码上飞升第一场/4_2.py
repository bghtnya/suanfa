m, k = map(int, input().split())
l = max((m + 3) // 2, m - k + 1)
r = (2 * m - k + 1) // 2
print(max(0, r - l + 1))
