#baekjoon 1932
n = int(input())
ary = []

for i in range(n):
    ary.append(list(map(int, input().split() )))

for row in range(1, n):
    # 2번째 줄부터 
    for idx in range(row + 1):
        # 줄이 왼쪽에 있을떄 자기 위에 있는것을 더한다.
        if idx == 0:
            ary[row][idx] = ary[row][idx] + ary[row - 1][idx]
        # 줄이 오른쪽에 있을때 자기 위에 있는것을 더한다. 
        elif idx == row :
            ary[row][idx] = ary[row][idx] + ary[row - 1][idx  - 1]
        # 중간에 있다면 
        else :
            ary[row][idx] = ary[row][idx] + max(ary[row - 1][idx - 1], ary[row - 1][idx])

print(max(ary[-1]))