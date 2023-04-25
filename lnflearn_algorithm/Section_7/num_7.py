'''Num_7: 송아지 찾기(BFS)'''
import sys
from collections import deque
sys.stdin=open('input.txt', 'r')
s, e = map(int, input().split())
Max = 1000
ch = [0]*(Max+1)
dis = [0]*(Max+1)
dis[s] = 0
dQ = deque()
dQ.append(s)
ch[s] = 1
i = 1
while dQ:
    tmp = dQ.popleft()
    if tmp == e:
        print(dis[tmp])
        break
    for nnext in (tmp-1, tmp+1, tmp+5): # 상태트리 뻗기 
        if 0< nnext <= Max:
            if ch[nnext] == 0:
                dQ.append(nnext)
                dis[nnext] = dis[tmp] + 1