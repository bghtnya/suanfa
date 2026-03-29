mem = {1: 1}

def bb(n):
    path, cur, mx = [], n, n
    while cur not in mem:
        path.append(cur)
        cur = cur // 2 if cur % 2 == 0 else cur * 3 + 1
        mx = max(mx, cur)
    mx = max(mx, mem[cur])
    for x in path:
        mem[x] = mx
    return mx

n = int(input())
ans = 1
for i in range(n, 0, -1):
    if i not in mem:
        ans = max(ans, bb(i))
print(ans)
