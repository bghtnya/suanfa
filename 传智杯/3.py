mod=10007

s=input().strip()
nums=[]
i=0
n=len(s)

while i<n:
    if s[i]=='(':
        sign=1
        if s[i+2]=='-':
            sign=-1
        d=int(s[i+3])
        nums.append(sign*d)
        i+=5
    else:
        i+=1

product=1
for a in nums:
    product=(product*a)%mod

def mod_inv(x):
    return pow(x,mod-2,mod)

ans=0
for a in nums:
    ans=(ans+product*mod_inv(a))%mod
print(ans%mod)