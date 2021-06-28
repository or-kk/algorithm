#baekjoon 11054
n = int(input())
ary = list(map(int, input().split()))

dp = [1] * n
rdp = [1] * n
result = [0] * n

for i in range(n):
    for j in range(i):
        if ary[i] > ary[j]:
                dp[i] = max(dp[i], dp[j] + 1)                       

for i in range(n-1, -1, -1):
    for j in range(n-1, i, -1):
        if ary[i] > ary[j]:
            rdp[i] = max(rdp[i], rdp[j] + 1)

for i in range(n):
    result[i] = dp[i] + rdp[i] 

print(max(result) - 1)

