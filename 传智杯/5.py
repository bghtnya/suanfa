s = input().strip()
n = len(s)

ans = l = 0
last_r = last_e = -1

for i, ch in enumerate(s):
    if ch == 'd':
        l = i + 1
        last_r = last_e = -1
        continue

    if ch == 'r':
        last_r = i
    elif ch == 'e':
        last_e = i

    if last_r != -1 and last_e != -1:
        ans += max(0, min(last_r, last_e) - l + 1)

print(ans)
