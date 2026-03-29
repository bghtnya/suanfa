n = int(input())
sae = []
for i in range(n):
    s, a, e = map(int, input().split())
    sae.append((s, a, e))
sae.sort(key=lambda x: sum(x))

#print(sae)
t = {}
for i in range(n):
    if i == 0:
        t[i] = sae[i][0] + sae[i][1]
    else:
        t[i] = t[i - 1] + sae[i - 1][2] + sae[i][0] + sae[i][1]

print(sum(t.values()))
