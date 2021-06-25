#baekjoon 2759
n = int(input())

ary = [0] * 301 
dp = [0] * 301

for i in range(n):
    ary[i] = int(input())

dp[0] = ary[0]
dp[1] = ary[0] + ary[1]
dp[2] = max(ary[1] + ary[2], ary[0] + ary[2])

for i in range(3, n): 
    dp[i] = max(ary[i - 1] + ary[i] + dp[i - 3], ary[i] + dp[i - 2])

print(dp[n - 1])
