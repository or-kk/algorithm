#baekjoon 11066
import math

def solve():
    n = int(input())
    ary = list(map(int, input().split()))
    dp = [[0 for _ in range(n)] for _ in range(n)]
    for j in range(1, n):
        for i in range(j - 1, -1, -1):
            min_vale = math.inf
            for k in range(j-i):
                min_vale = min(min_vale, dp[i][i+k] + dp[i+k+1][j])
            dp[i][j] = min_vale + sum(ary[i:j+1])
            
    print(dp[0][n-1])    

tc = int(input())
for _ in range(tc):
    solve()