'''Num_2: 랜선 자르기_Try_2'''
import sys
sys.stdin=open('input.txt','r')
k, n = map(int,input().split())
a = []
for _ in range(k):
    tmp = int(input())
    a.append(tmp)
Max = max(a)
def Count(length:int) -> int:
    cnt = 0
    for x in a:
        cnt += x//length
    return cnt
left = 1
right = Max
res = 0
while left <= right:
    mid = (left+right)//2
    if Count(mid) >= n:
        res = mid
        left = mid + 1
    else:
        right = mid - 1
print(res)
