n,t=map(int,input().split())
c=input()
cqwq=[]

def change(c):
    d=''
    for i in range(len(c)):
        if i==0:
            d=c[0]
            continue
        d+='0' if c[i]==c[i-1] else '1'
    return d
for _ in range(t):
    c=change(c)
    if c in cqwq:
       c=cqwq[t%len(cqwq)-1]
       break
    cqwq.append(c)
print(c)
