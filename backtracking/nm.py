#baekjoon 15649
n, m = map(int, input().split())
visited = [False] * n
result = []

def DFS(depth, n, m):
    if m == depth :
        print(' '.join(map(str, result)))
        return  

    for i in range(n):
        if not visited[i] :
            visited[i] = True
            result.append(i + 1)
            DFS(depth + 1, n, m)
            visited[i] = False
            result.pop()
    
DFS(0, n, m)