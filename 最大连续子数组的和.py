a = [-2, 1, -3, 4, -1, 2, 1, -5, 4]

mx = c = 0
for i in a:
    c = max(i, c + i)
    mx = max(mx, c)
print(mx)

