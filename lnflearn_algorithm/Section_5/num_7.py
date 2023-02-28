'''Num_7: 교육과정 설계 (Queue)'''
import sys
from collections import deque
sys.stdin=open('input.txt', 'r')
c = input()
n = int(input())
for _ in range(n):
    dq = deque(c)
    sub = input()
    for x in sub:
        if x in dq:
            if x != dq.popleft():
                print('NO')
                break
            else:
                if len(dq) == 0:
                    print('YES')
                    break
                


