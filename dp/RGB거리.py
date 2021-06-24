#baekjoon 1149
import sys

n = int(sys.stdin.readline())
ary = []
r, g, b = map(int, sys.stdin.readline().split())
ary.append((r, g, b))

for _ in range(1, n):
    r, g, b = map(int, sys.stdin.readline().split())
    
    pr, pg, pb = ary[-1]
    R = r + min(pg, pb)
    G = g + min(pr, pb)
    B = b + min(pr, pg)    

    ary.append((R,G,B))
    
r,g,b = ary[-1]
print(min(r,g,b))
