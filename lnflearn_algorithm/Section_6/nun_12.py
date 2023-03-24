'''Num_12: 인접행렬 (weighted directed graph)'''
import sys
sys.stdin=open('input.txt', 'r')
n, m = map(int, input().split())
a = [[0]*n for _ in range(n)]
for _ in range(m):
    n1, n2, w = map(int, input().split())
    a[n1-1][n2-1] = w
for x in a:
    print(*x)