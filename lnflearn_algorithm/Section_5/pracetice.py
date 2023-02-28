#import sys
#input = sys.stdin.readline
# index
# 1021 python
from collections import deque
import sys
sys.stdin=open('input.txt', 'r')
n, m = map(int, input().split())
loc = list(map(int, input().split()))
# python deque rotation : deque를 좌우로 회전할 수 있음
# +: 오른쪽, -: 왼쪽
nums = list(range(1, n+1))
dq = deque(nums)
cnt = 0
for x in loc:
    while True:
        left = dq[0]
        right = dq[-1]
        mid = (left+right)//2
        if x == dq[0]:
            dq.popleft()
            break
        else:
            if x > mid:
                dq.rotate(1)
                cnt += 1
            else:
                dq.rotate(-1)
                cnt += 1
print(cnt)
            
