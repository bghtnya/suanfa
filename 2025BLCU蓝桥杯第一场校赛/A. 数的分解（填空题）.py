c=0
for i in range(1,2020):
    if '2' in str(i) or '4' in str(i):
        continue
    for j in range(i+1, 2020):
        if '2' in str(j) or '4' in str(j):
            continue
        for k in range(j+1, 2020):
            if '2' in str(k) or '4' in str(k):
                continue
            if i+j+k==2019:
                c+=1

print(c)