s = input()
ss = ''
for i in s:
    if i.isdigit():
        ss += ss[-1] * (int(i) - 1)
    else:
        ss += i
print(ss)
