# Python_Itertools: https://seu11ee.tistory.com/5 -> Brute-force 이외의 사용
import sys
from collections import deque
sys.stdin=open('input.txt', 'r')
n, m = map(int, input().split())
dq = [(pos, val) for pos, val in enumerate(list(map(int, input().split())))]
dq = deque(dq)
cnt = 0
while True:
    cur = dq.popleft()
    if any(cur[1] < x[1] for x in dq):
        dq.append(cur)
    else:
        cnt += 1
        if cur[0] == m:
            print(cnt)
            break
        


#import sys
#input = sys.stdin.readline