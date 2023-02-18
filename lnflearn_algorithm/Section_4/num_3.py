'''Num_3: 뮤직비디오(결정알고리즘)'''
import sys
sys.stdin=open('input.txt', 'r')
n, m = map(int, input().split())
length = list(map(int, input().split()))
def DVD_Count(DVD_length: int) -> int:
    cnt = 1
    tot = 0
    for x in length:
        if tot+x > DVD_length:
            cnt += 1
            tot = x
        else:
            tot += x
    return cnt
left = 1
right = sum(length)
res = 0
while left <= right:
    mid = (left+right)//2
    if DVD_Count(mid) <= m:
        res = mid
        right = mid - 1
    else:
        left = mid + 1
print(res)