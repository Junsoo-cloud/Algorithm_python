from itertools import combinations
import sys
sys.stdin=open('input.txt', 'r')
n, m = map(int, input().split())
s = list(range(1, n))

for i in combinations(s, 2):
    print(*i)