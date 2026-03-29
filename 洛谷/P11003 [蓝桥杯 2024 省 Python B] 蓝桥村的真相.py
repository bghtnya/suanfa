T = int(input())
n = [int(input()) for _ in range(T)]

for i in n:
    if i % 3 == 0:
        c = 2 * i
    else:
        c = i
    print(c)
