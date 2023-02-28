'''Num_6: 응급실(Queue)'''
import sys
from collections import deque
sys.stdin=open('input.txt', 'r')
n, m = map(int, input().split())
dq = [(pos, val) for pos, val in enumerate(list(map(int, input().split())))]
dq = deque(dq)
cnt = 0
while True:
    cur = dq.popleft()
    if any(cur[1] < x[1] for x in dq): # any() : 안에 있는 조건이 하나라도 성립하면 참
        dq.append(cur)
    else:
        cnt += 1
        if cur[0] == m:
            print(cnt)
            break
        