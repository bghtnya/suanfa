import random
import sys
sys.setrecursionlimit(1000000)

def mul(a, b, mod): return a * b % mod

def qpow(a, b, mod):
    r = 1
    while b:
        if b & 1: r = mul(r, a, mod)
        a = mul(a, a, mod)
        b >>= 1
    return r

def gcd(a, b): return a if b == 0 else gcd(b, a % b)

def pollard_rho(n):
    if n % 2 == 0: return 2
    x = y = 2; c = 1
    f = lambda x: (mul(x, x, n) + c) % n
    while True:
        x = f(x); y = f(f(y)); d = gcd(abs(x - y), n)
        if 1 < d < n: return d
        if d == n: x = y = random.randint(1, n-1); c = random.randint(1, n-1)

def exgcd(a, b):
    if b == 0: return 1, 0
    x, y = exgcd(b, a % b)
    return y, x - (a // b) * y

e, N, c = map(int, input().split())
p = pollard_rho(N); q = N // p
r = (p-1)*(q-1)
d, _ = exgcd(e, r); d = (d % r + r) % r
print(d, qpow(c, d, N))
