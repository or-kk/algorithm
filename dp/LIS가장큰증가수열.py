#baekjoon 11055
n = int(input())
ary = list(map(int, input().split()))

dp = [0] * n
dp[0] = ary[0]

for i in range(n):
    for j in range(i):
        if ary[i] > ary[j]:
            dp[i] = max(dp[i], dp[j] + ary[i])
        else :
            dp[i] = max(dp[i], ary[i])

print(max(dp))
