#baekjoon 14888
import sys

n = int(sys.stdin.readline())
nums = list(map(int, sys.stdin.readline().split()))
combi = [i for i in list(map(int, sys.stdin.readline().split()))]
mins = 1e9
maxs = -1e9

def DFS(depth, cal, op1, op2, op3, op4):
    global maxs
    global mins
    if depth == n:
        maxs = max(cal, maxs)
        mins = min(cal, mins)
        return
    else :
        if op1 > 0:
            DFS(depth + 1, cal + nums[depth], op1 - 1, op2, op3, op4) 
        if op2 > 0:
            DFS(depth + 1, cal - nums[depth], op1, op2 - 1, op3, op4) 
        if op3 > 0:
            DFS(depth + 1, cal * nums[depth], op1, op2, op3 - 1, op4) 
        if op4 > 0:   
            DFS(depth + 1, int(cal / nums[depth]), op1, op2, op3, op4 - 1) 

DFS(1, nums[0], combi[0], combi[1], combi[2], combi[3])

print(maxs)
print(mins)