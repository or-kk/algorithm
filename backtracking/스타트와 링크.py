#baekjoon 14889
import sys
from itertools import combinations
sys.setrecursionlimit(100000)

n = int(sys.stdin.readline())
array = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
player = [i for i in range(n)]
teams = []
for i in combinations(player, n // 2):
    teams.append(i)

team_lens = len(teams)
result = []

def DFS(depth):
    if depth == team_lens // 2:
        print(min(result))
        sys.exit(0)
    else:    
        start_team = 0
        rink_team = 0            

        for x in teams[depth]:
            for y in teams[depth]:
                start_team += array[x][y]     

        for l in teams[team_lens - 1 - depth]:
            for z in teams[team_lens - 1 - depth]:
                rink_team += array[l][z]

        result.append(abs(start_team - rink_team))
        DFS(depth + 1)

DFS(0) 