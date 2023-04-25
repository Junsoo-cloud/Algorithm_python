import sys
from collections import deque
sys.stdin=open('input.txt', 'r')
N, M = map(int, input().split())
Max = 10**5
dQ = deque()
dis = [0]*(Max+2)
ch = [0]*(Max+2)
dQ.append(N)
dis[N] = 0
ch[N] = 1
res = []
while dQ:
    tmp = dQ.popleft()
    if tmp == M:
        x = dis[tmp]
        print(x)
        break
    for nnext in (tmp-1, tmp+1, tmp*2):
        if nnext < Max: 
            if 0<= nnext<= Max and (ch[nnext] == 0 or dis[nnext] > dis[tmp] + 1):
                res.append(nnext)
                dQ.append(nnext)
                ch[nnext] = 1
                dis[nnext] += dis[tmp] + 1
