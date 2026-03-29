from collections import deque
A, B = deque(input().strip()), deque(input().strip())
d, t, s = [], 0, set()
while 1:
    st = (tuple(A), tuple(B), tuple(d), t)
    if st in s: print(-1); break
    s.add(st)
    p = A if t == 0 else B
    if not p: print(''.join(B if t == 0 else A)); break
    c = p.popleft();
    d.append(c)
    i = len(d) - 2
    while i >= 0 and d[i] != c: i -= 1
    if i >= 0:
        p.extend(reversed(d[i:])); del d[i:]
    else:
        if not p: print(''.join(B if t == 0 else A)); break
        t ^= 1
