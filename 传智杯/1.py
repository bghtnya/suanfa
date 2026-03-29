n, k = map(int, input().split())
s = input()

u = sum(1 for c in s if 'A'<=c<='Z')
l=n-u

k2=min(k,l)
u+=k2
r=k-k2

print(u-(r%2))
