# 파도반 수열
import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
cnt = 0
d = [0]*(101)
d[1] = 1
d[2] = 1
d[3] = 1
d[4] = 2
d[5] = 2
while cnt < T:
    n = int(input())
    if n >5:
        for i in range(6, n+1):
            d[i] = d[i-1] + d[i-5]
    print(d[n])
    cnt += 1