# 1로 만들기
import sys
sys.stdin = open('input.txt', 'r')

n = int(input())

d = [0]*1000001


d[1] = 0
d[2] = 1
d[3] = 1

for i in range(4, n+1):
    d[i] = d[i-1] + 1
    if i % 3 == 0:
        d[i] = min(d[i-1], d[i//3]) + 1
    if i % 2 == 0:
        d[i] = min(d[i-1], d[i//2]) + 1
    if i % 2 == 0 and i % 3 == 0:
        d[i] = min(d[i-1], d[i//2], d[i//3]) + 1
        
print(d[n])