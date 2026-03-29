n = int(input())
a = list(map(int, input().split()))
s = sum(a)
c = ans = 0
for x in a:
    c += x
    ans += x * (s - c)
print(ans)
