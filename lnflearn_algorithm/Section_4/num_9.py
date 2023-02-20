'''Num_9: 증가수열 만들기'''
import sys
from collections import deque
sys.stdin=open('input.txt', 'r')
n = int(input())
nums = list(map(int, input().split()))
res = ''
tmp = []
last = 0
left = 0
right = n-1
while left <= right:
    if nums[left] > last:
        tmp.append((nums[left], 'L'))
    if nums[right] > last:
        tmp.append((nums[right], 'R'))
    tmp.sort()
    if len(tmp) == 0:
        break
    else:
        res += tmp[0][1]
        last = tmp[0][0]
        if tmp[0][1] == 'L':
            left += 1
        else:
            right -= 1
    tmp.clear()
print(len(res))
print(res)