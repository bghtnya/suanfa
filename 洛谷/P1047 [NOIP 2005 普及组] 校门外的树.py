l, m = map(int, input().split())
s = [1] * (l + 1)
for _ in range(m):
    u, v = map(int, input().split())
    s[u:v + 1] = [0] * (v - u + 1)
print(sum(s))
