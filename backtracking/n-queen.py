#baekjoon 9663 
n = int(input())
col = [0] * (n + 1)
count = 0

def solve(depth, col):
    global count
    k = len(col) - 1       
    if (promising(depth, col)):
        if depth == k :
          count += 1
          return
        else :
            for i in range(1, k + 1):
                col[depth + 1] = i                 
                solve(depth + 1 , col)
            
def promising(depth, col):
    k = 1
    flag = True
    while k < depth and flag == True:
            if col[depth] == col[k] or depth - k == abs(col[depth] - col[k]) :
                flag = False
            k += 1    
    return flag

solve(0, col)
print(count)