import sys

data=input().split()
if not data:
    exit(0)

t=int(data[0])

for _ in range(t):
    line=sys.stdin.readline().strip()
    n,m,x,y=map(int,line.split())


    bit=[0]*(n+1)
    state=[True]*(n+1)
    def update(i,d):
        while i<=n:
            bit[i]+=d
            i+=i&-i
    def query(i):
        s=0
        while i>0:
            s+=bit[i]
            i-=i&-i
        return s

    for i in range(1,n+1):
        update(i,1)
    for _ in range(m):
        p=int(input())
        if state[p]:
            update(p,-1)
            state[p]=False
        else:
            update(p,1)
            state[p]=True

        c1=query(x)
        c2=query(n)-query(y-1)
        results=[]
        results.append(f"{c1} {c2}")
        sys.stdout.write('\n'.join(results) + '\n')