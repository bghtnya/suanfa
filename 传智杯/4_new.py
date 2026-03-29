mem = {1: 1}  # mem 是一个 记忆化存储 的字典，避免重复计算
def bb(n):
    path, cur, mx = [], n, n
    while cur not in mem:
        path.append(cur)
        cur = cur // 2 if cur % 2 == 0 else cur * 3 + 1
        if cur > mx:
            mx = cur
    mx = max(mx, mem[cur])
    for x in path:
        mem[x] = mx
    return mx

n = int(input())
ans = 1
for i in range(n, 0, -1):
    if i not in mem:
        ans = max(ans, bb(i))
    else:
        if mem[i] > ans:
            ans = mem[i]
print(ans)
