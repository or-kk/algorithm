#baekjoon 10819
import sys
from itertools import permutations
sys.setrecursionlimit(100000)

result = []
def DFS(depth):        
    if depth == len(teams):
        print(max(result))        
        return 
    else :                
        cal = 0        
        for i in range(0, len(teams[depth]) - 1):                                     
            cal += abs(ary[teams[depth][i]] - ary[teams[depth][i + 1]])
        result.append(cal)
        DFS(depth + 1)       

n = int(sys.stdin.readline())
ary = list(map(int, sys.stdin.readline().split()))
combi = list(permutations([i for i in range(n)], n))

teams = []
for i in combi:
    teams.append(list(i))

DFS(0)