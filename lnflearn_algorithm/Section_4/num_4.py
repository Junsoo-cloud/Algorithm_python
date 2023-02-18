'''Num_4: 마구간 정하기 (결정알고리즘)'''
import sys
sys.stdin=open('input.txt', 'r')
def Count(length: int) -> int:
    cnt = 1
    ep = x_n[0]
    for i in range(1, n):
        if x_n[i] - ep >= length: # 첫번째 요소를 설정하는게 중요
            cnt += 1
            ep = x_n[i]
    return cnt
n, c = map(int, input().split())
x_n = []
for _  in range(n):
    tmp = int(input())
    x_n.append(tmp)
x_n.sort()
res = 0
left = 1
right = max(x_n)
while left <= right:
    mid = (left+right)//2
    if Count(mid) >= c:
        res = mid
        left = mid + 1
    else:
        right = mid - 1
print(res)