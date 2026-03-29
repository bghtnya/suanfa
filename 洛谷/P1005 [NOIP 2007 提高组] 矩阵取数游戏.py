n, m = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(n)]

total = 0
for row in matrix:
    dp = [[0]*m for _ in range(m)]
    for length in range(1, m+1):
        for l in range(m-length+1):
            r = l+length-1
            k = m - (r-l)  # 第 k 次取数
            weight = 2 ** k
            if l == r:
                dp[l][r] = row[l] * weight
            else:
                dp[l][r] = max(
                    row[l]*weight + dp[l+1][r],
                    row[r]*weight + dp[l][r-1]
                )
    total += dp[0][m-1]

print(total)
