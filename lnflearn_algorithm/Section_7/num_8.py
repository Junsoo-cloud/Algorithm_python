'''Num_8: 사과나무 (BFS)'''
import sys
from collections import deque
sys.stdin=open('input.txt', 'r')
N = int(input())
apple = [list(map(int, input().split())) for _ in range(N)]
ch = [[0]*N for _ in range(N)]
dQ = deque()
ch[N//2][N//2] = 1
dQ.append((N//2, N//2))
dx = [-1, 0, 0, 1] # 한칸씩 동서남북으로 할때 유용함 !!
dy = [0, 1, -1, 0]
tot = apple[N//2][N//2]
L = 0
while dQ:
    if L == N//2:
        break
    size = len(dQ)
    for i in range(size):
        tmp = dQ.popleft()
        for j in range(4):
            x = tmp[0] + dx[j]
            y = tmp[1] + dy[j]
            if ch[x][y] == 0:
                dQ.append((x, y))
                ch[x][y] = 1
                tot += apple[x][y]
    L += 1 
print(tot)