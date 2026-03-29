n = int(input())
n = 20 if n > 20 else n

F = {1: 1, 2: 1}
for i in range(3, n + 2):
    F[i] = F[i - 1] + F[i - 2]
print("{0:.8f}".format(F[n] / F[n + 1]))
