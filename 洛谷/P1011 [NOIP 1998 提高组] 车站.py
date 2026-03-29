a, n, m, x = map(int, input().split())
if x<4:
    s=[a,a,2*a]
    print(s[x])
    exit(0)
p=[1,1]
for i in range(2,17):
    p.append(p[i-1]+p[i-2])
q=[0,a]
for i in range(2,17):
    q.append(q[i-1]+q[i-2])
u=[1]
for i in range(1,17):
    u.append(u[i - 1] + p[i])
v=[a*2]
for i in range(1,17):
    v.append(v[i-1]+q[i])
# print(u)
# print(v)
# print(len(u),len(v))
#print(u[n-5],v[n-5],m)
s=(m-v[n-5])//u[n-5]
print(u[x-4]*s+v[x-4])