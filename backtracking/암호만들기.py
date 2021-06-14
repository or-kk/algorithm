#baekjoon 1759
import sys

def dfs(depth, index):
    if depth == r: 
        vo, co = 0, 0
        for i in range(r):
            if temp[i] in 'aeiou':
                co += 1
            else :
                vo += 1
        if co >= 1 and vo >= 2:
            print(''.join(temp))
        return
    
    for i in range(index, len(chrs)):
        if visited[i] == 0:
            visited[i] = 1
            temp.append(chrs[i])
            dfs(depth +1, i +1)
            visited[i] = 0
            del temp[-1]

r,c = map(int, sys.stdin.readline().split(' '))
chrs = input().split()
visited = [0 for i in range(c)]
temp = []

dfs(0, 0)