#baekjoon 1912
n = int(input())
ary = list(map(int, input().split()))

dp = [ary[0]]

for i in range(len(ary) - 1):    
    dp.append(max(dp[i] + ary[i + 1], ary[i + 1]))

print(max(dp))