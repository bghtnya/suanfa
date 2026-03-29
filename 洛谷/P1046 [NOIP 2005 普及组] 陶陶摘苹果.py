h = list(map(int, input().split()))
h2 = int(input())

s = sum([1 for i in h if h2 + 30 >= i])
print(s)
