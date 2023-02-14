'''Num_8: 곳감'''
import sys
sys.stdin=open('input.txt', 'r')
n = int(input())
matrix = [list(map(int, input().split())) for _ in range(n)]
m = int(input())
for _ in range(m):
    ad = []
    a, b, c = map(int, input().split())
    if b == 0:
        for _ in range(c):
            ad.append(matrix[a-1].pop(0))
        matrix[a-1] += ad
    else:
        for _ in range(c):
            ad.append(matrix[a-1].pop())
        matrix[a-1] += ad
res = 0
s = 0
e = n-1
for i in range(n):
    for j in range(s,e+1):
        res += matrix[i][j]
    if i < n//2:
        s += 1
        e -= 1
    else:
        s -= 1
        e += 1
print(res)
        