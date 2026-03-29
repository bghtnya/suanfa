x1, y1, x2, y2 = map(int, input().split())
# B , 马

xy = [(x2, y2), (x2 - 2, y2 + 1), (x2 - 2, y2 - 1), (x2 + 2, y2 + 1), (x2 + 2, y2 - 1), (x2 + 1, y2 + 2),
      (x2 - 1, y2 + 2), (x2 + 1, y2 - 2), (x2 - 1, y2 - 2)]

dp = [[0] * (y1 + 1) for _ in range(x1 + 1)]
dp[0][0] = 1

for i in range(x1 + 1):
    for j in range(y1 + 1):
        if (i, j) in xy:
            continue
        if i > 0:
            dp[i][j] += dp[i - 1][j]
        if j > 0:
            dp[i][j] += dp[i][j - 1]

print(dp[x1][y1])
