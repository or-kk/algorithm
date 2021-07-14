#baekjoon 1915
n, m = map(int, input().split())

ary = [[0 for i in range(m + 1)] for j in range(n + 1)]
dp  = [[0 for i in range(m + 1)] for j in range(n + 1)]
res = 0 

for i in range(n):
    for idx, j in enumerate(list(map(int, list(input())))):
        ary[i + 1][idx + 1] = j

for i in range(1, n+1):
    for j in range(1, m+1):
        if ary[i][j] == 1:
            dp[i][j] = min(dp[i-1][j], dp[i-1][j-1], dp[i][j-1]) + 1
            res = max(dp[i][j], res)

print(res**2)