#baekjoon 2580
import sys

sudoku = [list(map(int, sys.stdin.readline().split())) for i in range(9)]
empty_space = [(i, j) for i in range(9) for j in range(9) if sudoku[i][j] == 0]

def prommising(nx, ny, idx):
    if idx in sudoku[nx]:
        return False
    
    for i in range(9):
        if sudoku[i][ny] == idx:
            return False
    
    nx = nx // 3 * 3
    ny = ny // 3 * 3
    for i in range(3):
        for j in range(3):
            if sudoku[nx + i][ny + j] == idx:
                return False 

    return True

def DFS(depth):
    if depth == len(empty_space):
        for i in sudoku:
            for j in i:
                print(j, end = ' ')
            print()
        sys.exit(0)
    else :
        for i in range(1, 10):
            nx = empty_space[depth][0]
            ny = empty_space[depth][1]
            if prommising(nx, ny, i):
                sudoku[nx][ny] = i
                DFS(depth + 1)
                sudoku[nx][ny] = 0
DFS(0)