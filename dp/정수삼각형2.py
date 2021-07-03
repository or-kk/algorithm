n = int(input())

ary = [[0 for i in range(n + 1)] for i in range(n + 1)]
dp = ary

for i in range(1, n + 1):
    temp = list(map(int, input().split()))
    for j in range(1, i + 1):
        ary[i][j] = temp[j -1]

for i in range(1, n + 1):
    for j in range(1, i + 1) :
        dp[i][j] = max(dp[i -1][j-1], dp[i-1][j]) + ary[i][j]


print(max(dp[-1])) 