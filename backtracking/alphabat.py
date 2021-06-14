#baekjoon 1987
import sys

def dfs(x, y, cnt):
    global cnto
    cnto = max(cnto, cnt)

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx >= 0 and ny >= 0 and nx < r and ny < c and visited[ord(ary[nx][ny]) - 65] == 0:
            visited[ord(ary[nx][ny]) - 65] = 1
            dfs(nx, ny, cnt + 1)
            visited[ord(ary[nx][ny]) - 65] = 0

r, c  = map(int, sys.stdin.readline().split(' '))
ary = [list(sys.stdin.readline().strip()) for _ in range(r)]
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

visited = [0] * 26
visited[ord(ary[0][0]) - 65] = 1

cnto = 1
dfs(0,0, cnto)
print(cnto)