'''Num_9: 봉우리'''
import sys
sys.stdin=open('input.txt', 'r')
n = int(input())
matrix = [list(map(int, input().split())) for _ in range(n)]
matrix.insert(0, [0]*n)
matrix.append([0]*n)
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
for i in range(7):
    matrix[i].insert(0, 0)
    matrix[i].append(0)
cnt = 0
for i in range(1, n+1):
    for j in range(1, n+1):
        if all(matrix[i][j] > matrix[i+dx[k]][j+dy[k]] for k in range(4)): # all함수로 모든 조건 만족시키는 경우에만 cnt 1 증가
            cnt += 1
print(cnt)