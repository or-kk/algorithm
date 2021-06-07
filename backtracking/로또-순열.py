#baejoon 6603
import sys 
from itertools import combinations

while(True):
    n = list(map(int, sys.stdin.readline().split(' ')))
    k = n[0]
    if k == 0 :
        break
    n.pop(0)
    for i in combinations(n, 6):
        print(' '.join(map(str, i)))
    print()
   