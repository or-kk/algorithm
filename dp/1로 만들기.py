#baekjoon 1463
import math 
n = int(input())

dp = [0, 0, 1, 1]

for i in range(4, n + 1):
    a, b, c = math.inf, math.inf, dp[i - 1]
    if i % 3 == 0:
        a = dp[i//3]
    if i % 2 == 0:
        b = dp[i//2]
    val = 1 + min(a, b, c)
    dp.append(val)

print(dp[n])