#baekjoon 9252

x = input().strip()
y = input().strip()

dp = [[""] * (len(y) + 1) for _ in range(len(x) + 1)]

for i in range(1, len(x) + 1):
    for j in range(1, len(y) + 1):
        if x[i - 1] == y[j - 1] :
            dp[i][j] = dp[i - 1][j - 1] + x[i - 1]            
        else :
            if len(dp[i - 1][j]) >= len(dp[i][j - 1]) :
                dp[i][j] = dp[i - 1][j]
            else:
                dp[i][j] = dp[i][j - 1]

print(len(dp[-1][-1]))
print(dp[-1][-1])