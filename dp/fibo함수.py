#baekjoon 1003
def fibo(n):
    zero = [1, 0]
    one  = [0, 1]
    
    if n <= 1:
        return

    if len(zero) < n:
        for i in range (2, n + 1):
            zero.append(zero[i - 2] + zero[i - 1])
            one.append(one[i - 2] + one[i - 1])

    return zero, one 

t = int(input())
zero, one = fibo(40)

for _ in range(t):
    n = int(input())
    print(zero[n], one[n])