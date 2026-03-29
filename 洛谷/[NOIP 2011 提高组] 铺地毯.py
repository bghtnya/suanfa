n = int(input())

dt = []

for i in range(n):
    a, b, g, k = map(int, input().split())
    dt.append([i, a, b, g, k])
    #          0  1  2  3  4

c = []

x, y = map(int, input().split())
for t in dt:
    if x >= t[1] and x <= t[1] + t[3] and y >= t[2] and y <= t[2] + t[4]:
        c.append(t[0] + 1)

try:
    print(max(c))
except:
    print(-1)
