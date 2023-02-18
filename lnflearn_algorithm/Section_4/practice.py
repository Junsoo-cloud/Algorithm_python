import sys
sys.stdin=open('input.txt', 'r')
def Count_length(length: int) -> int:
    tot = 0
    for x in trees:
        if x >= length:
            tot += x-length
    return tot
n, m = map(int, input().split())
trees = list(map(int, input().split()))
left = 1
right = max(trees)
res = 0
while left <= right:
    mid = (left+right)//2
    if Count_length(mid) >= m:
        res = mid
        left = mid + 1
    else:
        right = mid - 1
print(res)