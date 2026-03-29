import math

n,k=map(int,input().split())
hw=[]
qwq=[]
square=[]
for _ in range(n):
    h,w=map(int,input().split())
    square.append(h*w)
    hw.append((h,w))
    qwq.append(h)
    qwq.append(w)
#print(hw,k)

m=min(qwq)
if m<=1:
    print(1)
    exit(0)

if k==1:
    print(m)
else:
    owo=min(m,math.isqrt(sum(square) // k),math.isqrt(min(square)))
    print(owo)