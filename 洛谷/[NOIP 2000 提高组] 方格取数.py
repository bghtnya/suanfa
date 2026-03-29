n = int(input())
p = [[0] * (n + 1) for _ in range(n + 1)]

while 1:
    a, b, c = map(int, input().split())
    if a == b == c == 0:
        break
    p[a][b] = c

dp = [[[-1] * (n + 1) for _ in range(n + 1)] for _ in range(2 * n + 1)]
dp[2][1][1] = p[1][1]

for k in range(3, 2 * n + 1):
    for x1 in range(1, n + 1):
        y1 = k - x1
        for x2 in range(1, n + 1):
            y2 = k - x2
            if y1 > n or y2 > n:
                continue

            for px1, px2 in ((x1 - 1, x2 - 1), (x1 - 1, x2), (x1, x2 - 1), (x1, x2)):
                py1 = k - 1 - px1
                py2 = k - 1 - px2
                if py1 > n or py2 > n:
                    continue
                dp[k][x1][x2] = max(dp[k][x1][x2], dp[k - 1][px1][px2])
            if dp[k][x1][x2] == -1:
                continue
            if x1 == x2 or y1 == y2:
                dp[k][x1][x2] += p[x1][y1]
            else:
                dp[k][x1][x2] += p[x1][y1] + p[x2][y2]
print(dp[2 * n][n][n])
