
def if2025(n):
    s=[0]*10
    for i in str(n):
        s[int(i)]+=1
    return s[2]>=2 and s[0]>=1 and s[5]>=1


c=0
for i in range(2026):
    if if2025(i):
        c+=1
print(c)
