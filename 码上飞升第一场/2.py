import math
n = int(input())

is_prime = [True] * (n + 1)
is_prime[0] = is_prime[1] = False
for i in range(2, int(math.sqrt(n)) + 1):
    if is_prime[i]:
        for j in range(i * i, n + 1, i):
            is_prime[j] = False

for i in range(4, n + 1, 2):
    for a in range(2, i // 2 + 1):
        b = i - a
        if is_prime[a] and is_prime[b]:
            print(f"{i}={a}+{b}")
            break
