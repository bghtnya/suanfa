l = int(input())
n = int(input())
if n == 0:
    print('0 0')
    exit(0)
allx = list(map(int, input().split()))
mn = mx = 0
for x in allx:
    mn = max(mn, min(x, l + 1 - x))
    mx = max(mx, max(x, l + 1 - x))
print(mn, mx)
