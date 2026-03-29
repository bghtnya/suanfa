n = int(input())
c = 0
for i in range(10, 10 ** 7):
    j = [int(j) for j in str(i)]

    m = True
    for k in range(1, len(j)):
        if j[k] % 2 == j[k - 1] % 2:
            m = False
            break
    if m:
        c += 1
        if c == n:
            print(i)
            exit(0)
