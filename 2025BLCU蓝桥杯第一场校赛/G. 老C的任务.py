n,m=map(int,input().split())
jz=[]
for _ in range(n):
    jz.append(list(map(int, input().split())))

for _ in range(m):
    x1,y1,x2,y2=map(int, input().split())
    sp=0
    for cjz in jz:
        x=cjz[0]
        y=cjz[1]
        p=cjz[2]
        if x1<=x<=x2 and y1<=y<=y2:
            sp+=p
    print(sp)


