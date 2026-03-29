def extended_gcd(a, b):
    if a == 0:
        return b, 0, 1
    d, x1, y1 = extended_gcd(b % a, a)
    x = y1 - (b // a) * x1
    y = x1
    return d, x, y


def crt(a_list, m_list):
    M = 1
    for m in m_list:
        M *= m

    ans = 0
    for a, m in zip(a_list, m_list):
        Mi = M // m
        _, ti, _ = extended_gcd(Mi, m)
        ans = (ans + a * Mi * ti) % M

    return (ans + M) % M


n = int(input())
m_list = []
a_list = []
for _ in range(n):
    m, a = map(int, input().split())
    m_list.append(m)
    a_list.append(a)

print(crt(a_list, m_list))