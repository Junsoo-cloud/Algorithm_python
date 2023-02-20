'''Num_8: 침몰하는 타이타닉(그리디 알고리즘)'''
# deque() 사용 -> from collections import deque
# deque 공부 필요
# deque는 list와 대비되게 데이터를 다 옮길 필요 없이 포인터만 옮겨짐
import sys
from collections import deque
sys.stdin=open('input.txt', 'r')
n, m = map(int, input().split())
weight = list(map(int, input().split()))
weight.sort()
weight = deque(weight)
cnt = 0
while weight:
    if len(weight) == 1:
        cnt += 1
        break
    if weight[0] + weight[-1] > m:
        weight.pop()
        cnt += 1
    else:
        weight.pop()
        weight.popleft()
        cnt += 1
print(cnt)