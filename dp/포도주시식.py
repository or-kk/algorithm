#baekjoon 2156
n = int(input())
dp = [0]
ary = [0]

for i in range(n):
    ary.append(int(input()))

dp.append(ary[0])
if n > 1 :    
    dp.append(ary[1] + ary[2])
    

for i in range(3, n + 1):
    dp.append(max(dp[i - 1], dp[i - 2] + ary[i], ary[i] + ary[i - 1] + dp[i - 3]))
    
print(dp[n])