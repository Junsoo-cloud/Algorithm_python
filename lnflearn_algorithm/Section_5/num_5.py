'''Num_5: 공주 구하기(Queue)'''
import sys
from collections import deque
sys.stdin=open('input.txt', 'r')
n, k = map(int, input().split())
queue = list(range(1, n+1))
queue = deque(queue)
while len(queue) > 1:
    for _ in range(k-1):
        n1 = queue.popleft()
        queue.append(n1)
    queue.popleft()
print(queue[0])