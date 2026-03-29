n = input()
s = 0
for i in range(len(n) + 1):
    for j in range(i + 2, len(n) + 1):
        nn = n[:i] + n[i:j][::-1] + n[j:]
        if nn < n:
            s += 1
        #print(n[i:j], n[i:j][::-1], int(n), int(nn), s)
print(s)
