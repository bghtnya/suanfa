moves = (1, 3, 7, 8)
f = [0] * 10001

for i in range(1, 10001):
    f[i] = any(i - x > 0 and f[i - x] == 0 for x in moves)

for _ in range(int(input())):
    print(1 if f[int(input())] else 0)
