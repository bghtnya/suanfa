n=int(input())
s=0
for i in range(1,n+1):
    s+=i*(n-i)**2
print(s%(10**9+7))