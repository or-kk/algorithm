#baekjoon 12849

d = int(input())

dp = [1,0,0,0,0,0,0,0] 

def next(step):
    tmp = [0 for _ in range(8)]
    tmp[0] = step[1] + step[2]
    tmp[1] = step[0] + step[2] + step[3]
    tmp[2] = step[0] + step[1] + step[3] + step[4]
    tmp[3] = step[1] + step[2] + step[4] + step[5]
    tmp[4] = step[2] + step[3] + step[5] + step[7]
    tmp[5] = step[3] + step[4] + step[6]
    tmp[6] = step[5] + step[7]
    tmp[7] = step[4] + step[6]
    for i in range(8):
        tmp[i] %= 1000000007
    return tmp

for i in range(d):
    dp = next(dp)

print(dp[0])