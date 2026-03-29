n = int(input())
a = map(int, input().split())
mod = 10 ** 9 + 7
from collections import Counter

cnt = Counter(a)
vals = list(cnt.keys())
ans = 0

for x in vals:
    for y in vals:
        if x != y:
            ans += cnt[x] * (cnt[x] - 1) * cnt[y] * (cnt[y] - 1)
        elif x == y:
            c = cnt[x]
            ans += c * (c - 1) * (c - 2) * (c - 3)
print(ans % mod)
