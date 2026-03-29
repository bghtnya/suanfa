for i in range(123, 333):
    s = str(i) + str(i * 2) + str(i * 3)
    if '0' not in s and len(set(s)) == 9:
        print(i, i * 2, i * 3)
