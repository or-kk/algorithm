import sys 

def DFS(depth, idx):
    if depth == 6:
        print(' '.join(map(str,visited)))
        return
    
    for i in range(idx, len(n)):
        visited[depth] = n[i]
        DFS(depth + 1, i + 1)


while(True):
    n = list(map(int, sys.stdin.readline().split(' ')))
    k = n[0]
    if k == 0 :
        break
    n.pop(0)
    visited = [0] * 6
    DFS(0, 0)
    print()
