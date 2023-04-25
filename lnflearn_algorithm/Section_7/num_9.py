'''Num_9: 미로 찾기 (BFS)'''
import sys
from collections import deque
sys.stdin=open('input.txt', 'r')
matrix = [list(map(int, input().split())) for _ in range(7)]
ch = [[0]*7 for _ in range(7)]
dQ = deque()
dQ.append((0, 0))
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]
matrix[0][0] = 1
cnt = 0
while dQ:
    tmp = dQ.popleft()
    for i in range(4):
        x = tmp[0] + dx[i]
        y = tmp[1] + dy[i]
    if 0<=x<=6 and 0<=y<=6 and matrix[x][y] == 0:
        if ch[x][y] == 0:
            matrix[x][y] = 1
            dQ.append((x,y))
            cnt += 1
            ch[x][y] = 1
print(cnt)