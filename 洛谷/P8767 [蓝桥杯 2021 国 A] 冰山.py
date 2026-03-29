# n, m, k = map(int, input().split())
# bs = list(map(int, input().split()))
# for _ in range(m):
#     xy = list(map(int, input().split()))
#     for i in range(len(bs)):
#         bs[i] += xy[0]
#         if bs[i] >= k:
#             bs += (bs[i] - k) * [1]
#             bs[i] = k
#     bs += [xy[1]]
#     print(sum(bs) % 998244353)

n, m, k = map(int, input().split())
bs = list(map(int, input().split()))
bss = sum(bs)
bsl = len(bs)
for _ in range(m):
    xy = list(map(int, input().split()))
    bss += bsl * xy[0]
