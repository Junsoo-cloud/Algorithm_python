'''Num_9: 봉우리'''
import sys
sys.stdin=open('input.txt', 'r')
n = int(input())
matrix = [list(map(int, input().split())) for _ in range(n)]
for i in range(n):
    for j in range(n):
        