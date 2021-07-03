#baekjoon 11055
import copy 
n = int(input())
ary = list(map(int,input().split()))
dp = copy.deepcopy(ary)

for i in range(1, n):
    for j in range(i):        
        if ary[i] > ary[j]:
            dp[i] = max(dp[i], dp[j] + ary[i])

print(max(dp))