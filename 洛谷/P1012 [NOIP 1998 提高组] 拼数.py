input()
a = input().split()

from functools import cmp_to_key
def cp(a, b):
    if a + b > b + a:
        return -1
    elif a + b < b + a:
        return 1
    else:
        return 0
a.sort(key=cmp_to_key(cp))
print(''.join(a))
