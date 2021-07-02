#baekjoon 2565
n  = int(input())
dp = [1] * n

ary = [list(map(int, input().split())) for _ in range(n)]
ary = sorted(ary, key = lambda x:x[0])

for i in range(n):
    for j in range(i):
        if ary[i][1] > ary[j][1]:
            dp[i] = max(dp[j] + 1, dp[i])
            
print(n - max(dp))